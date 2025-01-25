from flask import Flask, render_template, Response
import cv2
import mediapipe as mp
import os
from inference_sdk import InferenceHTTPClient
from dotenv import load_dotenv
from distraction_detection import get_gaze_direction, check_distraction, detect_objects

# Load variables from the .env file
load_dotenv()
ROBOFLOW_API_KEY = os.getenv("ROBOFLOW_API_KEY")

# --- Roboflow API Configuration ---
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key=ROBOFLOW_API_KEY
)

# --- Initialize Face Mesh Model ---
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

app = Flask(__name__)

@app.route('/')
def home():
    """Render home page with 'Begin Working!' button."""
    return render_template('home.html')

@app.route('/begin_working')
def begin_working():
    """Render the distraction detection page."""
    return render_template('index.html')

# Streaming video from webcam
def gen_video():
    """Generate video stream."""
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process face landmarks
        results = face_mesh.process(rgb_frame)
        detected_objects = detect_objects(frame)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                gaze_direction = get_gaze_direction(face_landmarks)
                distraction_status = check_distraction(gaze_direction, detected_objects)

                # Display gaze direction and distraction status
                cv2.putText(frame, f"Gaze: {gaze_direction}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.putText(frame, f"Status: {distraction_status}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Convert frame to JPEG
        _, jpeg = cv2.imencode('.jpg', frame)
        frame = jpeg.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    """Stream the webcam feed to the browser."""
    return Response(gen_video(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)

import cv2
import mediapipe as mp
import requests
import base64
import streamlit as st
from dotenv import load_dotenv
import os
from inference_sdk import InferenceHTTPClient

load_dotenv()  # Load variables from the .env file
ROBOFLOW_API_KEY = os.getenv("ROBOFLOW_API_KEY")

# --- Roboflow API Configuration ---
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key=ROBOFLOW_API_KEY
)

# --- Initialize Face Mesh Model ---
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

st.title("Pomodoro Timer: Begin Working")

frame_placeholder = st.empty()

stop_button_pressed = st.button('Stop')

def detect_objects(frame):
    _, buffer = cv2.imencode('.jpg', frame)  # Encode frame as JPEG
    encoded_image = base64.b64encode(buffer).decode('utf-8')  # Convert to base64 string
    
    result = CLIENT.infer(encoded_image, model_id="coco/3")  # Use your model ID
    
    detected_objects = []
    for obj in result["predictions"]:
        label = obj["class"]
        x, y, w, h = obj["x"], obj["y"], obj["width"], obj["height"]
        x1, y1 = int(x - w / 2), int(y - h / 2)
        x2, y2 = int(x + w / 2), int(y + h / 2)
        detected_objects.append({"label": label, "bbox": (x1, y1, x2, y2)})
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return detected_objects

# --- Improved Gaze Direction Detection ---
def get_gaze_direction(face_landmarks):
    left_eye_outer = face_landmarks.landmark[33]
    left_eye_inner = face_landmarks.landmark[133]
    left_pupil = face_landmarks.landmark[468]
    left_eye_bottom = face_landmarks.landmark[159]
    left_eye_top = face_landmarks.landmark[386]

    right_eye_outer = face_landmarks.landmark[362]
    right_eye_inner = face_landmarks.landmark[263]
    right_pupil = face_landmarks.landmark[473]
    right_eye_bottom = face_landmarks.landmark[386]
    right_eye_top = face_landmarks.landmark[159]

    left_eye_width = abs(left_eye_inner.x - left_eye_outer.x)
    right_eye_width = abs(right_eye_inner.x - right_eye_outer.x)

    left_pupil_offset_x = (left_pupil.x - left_eye_outer.x) / left_eye_width
    right_pupil_offset_x = (right_pupil.x - right_eye_outer.x) / right_eye_width

    left_pupil_offset_y = (left_pupil.y - left_eye_bottom.y) / (left_eye_top.y - left_eye_bottom.y)
    right_pupil_offset_y = (right_pupil.y - right_eye_bottom.y) / (right_eye_top.y - right_eye_bottom.y)

    gaze_offset_x = (left_pupil_offset_x + right_pupil_offset_x) / 2
    gaze_offset_y = (left_pupil_offset_y + right_pupil_offset_y) / 2

    down_threshold = 0.02
    up_threshold = -0.06

    if gaze_offset_x < 0.4:
        return "Looking Left"
    elif gaze_offset_x > 0.6:
        return "Looking Right"
    elif gaze_offset_y > down_threshold:
        return "Looking Down"
    elif gaze_offset_y < up_threshold:
        return "Looking Up"
    else:
        return "Looking Center"

def check_distraction(gaze_direction, objects):
    phone_present = any(obj["label"] == "cell phone" for obj in objects)
    notebook_present = any(obj["label"] == "notebook" for obj in objects)

    if phone_present and gaze_direction == "Looking Down":
        return "DISTRACTED"
    elif notebook_present and gaze_direction == "Looking Down":
        return "NOT DISTRACTED"
    elif phone_present and notebook_present and gaze_direction == "Looking Down":
        return "DISTRACTED"
    else:
        return "FOCUSED"

# --- Webcam Feed Processing ---
cap = cv2.VideoCapture(0)

while cap.isOpened() and not stop_button_pressed:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_placeholder.image(frame, channels='RGB')
    results = face_mesh.process(rgb_frame)

    detected_objects = detect_objects(frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            gaze_direction = get_gaze_direction(face_landmarks)
            distraction_status = check_distraction(gaze_direction, detected_objects)

            cv2.putText(frame, f"Gaze: {gaze_direction}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, f"Status: {distraction_status}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the frame
    cv2.imshow("Distraction Detection", frame)

    # Handle ESC key press to stop
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC key to exit
        break
    elif cv2.getWindowProperty("Distraction Detection", cv2.WND_PROP_VISIBLE) < 1:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

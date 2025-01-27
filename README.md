# Flowcus



## Table of Contents
1. [Project Overview](#Project-Overview)
2. [Features](#Features)
3. [APIs and Technologies](#APIs-and-Technologies)
4. [Development Roadmap](#Development-Roadmap)
5. [Future Plans](#Future-Plans)
6. [Additional Information](#Additional-Information)


## 📚 Project Overview
Flowcus is a web application designed to enhance productivity by helping users stay focused on their tasks. By utilizing Computer Vision technologies like gaze tracking, pose estimation, and object detection, the app processes webcam data to detect distractions and ensure the user remains productive.

The project is currently in development and aims to combine the Pomodoro technique with real-time distraction detection to create a unique and effective productivity tool.

## 🛠️ Features

 - ***Task Management***
   - Users can create a list of tasks they aim to complete during their work session. These tasks can be added, edited, and managed directly within the application.

 - ***Pomodoro Timer***
   - Customizable Timer: The application includes a timer aligned with the Pomodoro technique to encourage focused work sessions.
   - Distraction Alerts: If the application detects user distraction, the timer will pause. An audio or visual alert will prompt the user to return to their tasks.

 - ***Distraction Detection***
   - The application leverages advanced Computer Vision technologies to monitor user focus and detect distractions in real time. Key components include:
     - ***Object Detection***:
       - Utilizes webcam input to identify distracting objects (e.g., a phone) within the user’s vicinity.
       - Recognizes physical work contexts, such as writing in a notebook.

     - ***Gaze Tracking***:
       - Analyzes the user’s gaze direction to assess focus. For example:
        - If a phone is detected and the user’s gaze is directed downward, the timer pauses, and an alert is triggered.
        - If a notebook is detected and the gaze is downward, the timer continues, recognizing active work.
        - A gaze directed at the screen also allows the timer to continue.

     - ***Pose Estimation***:
       - Assesses body posture to detect distractions when objects are out of the camera frame. For instance:
        - If the user is reclining and gazing downward, it may indicate phone use, prompting an alert.
        - If leaning forward and gazing downward, it infers work on a notebook, allowing the timer to continue.
        
     - ***Productivity Metrics***
       - Performance Statistics: The app provides detailed insights into user productivity, including:
         - Total time spent focused.
         - Duration of distractions.
         - Trends and patterns in work behavior over time.

## 💻 APIs and Technologies   
 - ***TensorFlow Object Detection API***: A robust framework for detecting objects in images and videos. In this project, it identifies distracting objects like phones or work-related items like notebooks to infer user focus.
 - ***GazeCloud API***: The GazeCloud API enables real-time eye tracking using a webcam, providing insights into user focus and engagement. It requires no extra hardware and supports applications like UX research, productivity tracking, and accessibility.
 - ***Google MediaPipe***: A powerful framework for real-time face and pose detection. MediaPipe is used for pose estimation to determine whether the user's posture indicates active work or distraction.



## Development Roadmap:

### **1. Researching Technologies & APIs**
- Conducted research on available computer vision libraries and APIs.
- Chose **Roboflow** for object detection and **MediaPipe** for gaze estimation.
- Selected **Flask** for the backend and **React** for the frontend.

### **2. Object Detection with Roboflow**
- Trained an object detection model on the **COCO dataset** using Roboflow.
- Integrated the model into the application using the **Roboflow API**.
- Tested object detection to ensure accurate identification of distractions like phones.

### **3. Gaze Estimation & Distraction Detection**
- Integrated **MediaPipe Face Mesh** to track eye movement and gaze direction.
- Developed logic to determine if the user is looking at their phone or another distraction.
- Combined object detection with gaze estimation to create a **distraction detection technique**.
- Validated that the model accurately differentiates between focus and distraction.

### **4. Building the Web Application**
- Developed a **Flask backend** to process real-time video data and send results to the frontend.
- Created a **React frontend** with a simple UI:
  - A landing page with a "Begin Working" button.
  - A workspace with a webcam feed and distraction alerts.
- Ensured seamless integration between Flask and the frontend.

### **5. Deployment & Documentation**
- Deployed the Flask backend and React frontend.
- Created a detailed **README** with setup instructions, usage guide, and development roadmap.
- Published the project on **GitHub** for accessibility and future improvements.



## Future Plans:
 - Implementing technologies to determine whether the user’s activity on the computer aligns with their tasks. For this project, simply focusing on the screen is considered as working.
 - Gamifying the Pomodoro technique by adding interactive elements, such as a boss health bar that depletes when tasks are completed, encouraging users to stay productive.
 - Enhancing accessibility with voice commands for smoother interaction.
 - Optimizing real-time performance to reduce latency and improve response times.

## ℹ️ Additional Information
 - This project is a feasibility study on the TensorFlow Object Detection API and the related technologies as part of the API Study URV program under the mentorship of Mr. Andre Kenneth 'Chase' Randall.


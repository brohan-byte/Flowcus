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
- Selected **Flask** for the backend.

### **2. Object Detection with Roboflow**
- Integrated an Object Deteection model trained on the COCO dataset into the application using the **Roboflow API**.
- Tested object detection to ensure accurate identification of distractions like phones.

### **3. Gaze Estimation & Distraction Detection**
- Integrated **MediaPipe Iris** to track eye movement and gaze direction.
- Developed logic to determine if the user is looking at their phone or another distraction.
- Combined object detection with gaze estimation to create a **distraction detection technique**.
- Validated that the model accurately differentiates between focus and distraction.

### **4. Building the Web Application**
- Developed a **Flask backend** to process real-time video data and send results to the frontend.
- Created a with a simple home-page using html to display the app functionality:
  - A landing page with a "Begin Working" button.
  - A workspace with a webcam feed and distraction alerts.
- Ensured seamless integration between Flask and the frontend.

### **5. Deployment & Documentation**
- Deployed the Flask backend and a simple html frontend page.
- Published the project on **GitHub** for accessibility and future improvements.



## Future Development Roadmap:
### **6. Task Alignment & Smarter Focus Detection**
   - Expanding beyond basic gaze tracking by developing a system that analyzes the user’s on-screen activity.
   - Ensuring that simply looking at the screen is not enough— the system will verify whether the user’s active tasks align with their intended work.
   - Exploring integrations with productivity apps and task managers to provide contextual insights on focus and workflow.
  
### ** Gamification & User Engagement** 
   - Enhancing the Pomodoro experience by introducing interactive elements to make productivity more engaging.
   - Implementing a "boss health bar" that depletes as the user completes tasks, rewarding focus and discipline.
   - Potentially adding streak tracking and achievement badges to encourage long-term habit formation.

### **Accessibility & Performance Enhancements** 
   - Introducing voice command functionality to improve accessibility, allowing hands-free interaction with the app.
   - Optimizing real-time processing to reduce latency and enhance responsiveness.
   - Refining distraction detection to work more efficiently across different lighting conditions and camera qualities.

## ℹ️ Additional Information
 - This project is a feasibility study on the TensorFlow Object Detection API and the related technologies as part of the API Study URV program under the mentorship of Mr. Andre Kenneth 'Chase' Randall.


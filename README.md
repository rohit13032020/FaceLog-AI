FaceLog-AI — AI-Powered Attendance Management System

FaceLog-AI is an intelligent attendance management system designed to simplify and modernize attendance tracking using Artificial Intelligence (AI), facial recognition, and voice recognition technologies. The project uses Python and Streamlit to provide an interactive user interface, while Supabase supports database integration.

Features

AI-Based Face Recognition: Identify registered individuals using facial recognition technology.

Automated Attendance: Simplify attendance recording through AI-powered identification.

Voice Recognition: Use voice-processing technologies for speaker recognition.

Database Integration: Manage application data using Supabase.

Interactive User Interface: Access application features through a Streamlit interface.

Secure Password Handling: Use bcrypt for password hashing.

Image Processing: Process images using Pillow.

Audio Processing: Analyze audio signals using Librosa and Resemblyzer.


Tech Stack

Programming Language

Python

Frontend and Application Framework

Streamlit

Data Processing

NumPy

Pandas

Face Recognition and Machine Learning

Scikit-learn

dlib-bin

face_recognition_models

Voice Recognition and Audio Processing

Librosa

Resemblyzer

Database and Security

Supabase

bcrypt

Image Processing and Utilities

Pillow

Segno

Setuptools


Prerequisites

Before running the project, make sure you have:

Python installed on your system.

Git installed on your system.

A Supabase account and project.

A compatible environment for installing the face recognition and audio processing dependencies.


Installation and Setup

1. Clone the Repository

```bash
git clone https://github.com/rohit13032020/FaceLog-AI.git
```

2. Navigate to the Project Directory

```bash
cd FaceLog-AI
```

3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment.

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

4. Install Dependencies

Make sure your requirements.txt file contains the project's dependencies.

```bash
pip install -r requirements.txt
```

Note: Installing dlib-bin, face_recognition_models, Librosa, and Resemblyzer may require compatible Python versions and system dependencies.

5. Configure Supabase

1. Create a project in Supabase.
2. Configure the required database tables according to the project code.
3. Add the Supabase project URL and required API key to your environment configuration.
4. Keep your credentials private. Do not commit API keys, passwords, or other secrets to GitHub.

6. Run the Application

If the main application file is named app.py, run:

streamlit run app.py

If your entry-point file has a different name, replace app.py with the correct filename.

Security

Store credentials in environment variables or a secure secrets configuration.

Never expose Supabase service-role keys in frontend code or public repositories.

Use bcrypt for password hashing rather than storing plain-text passwords.

Configure appropriate database access policies to protect student and attendance records.

Project Objective

The primary objective of FaceLog-AI is to reduce manual attendance work by using AI-powered identification and automated record management. The project combines facial recognition, voice-processing technologies, and database integration to explore a more efficient approach to attendance management.

Developer

Rohit Jana

GitHub: https://github.com/rohit13032020
website urls : https://facelogai-main.streamlit.app/
Future Enhancements

Improve face recognition accuracy and reliability.

Enhance attendance reporting and analytics.

Improve authentication and access control.

Expand voice recognition capabilities.

Improve the user interface and overall application performance.

If you find this project interesting, consider giving the repository a star.

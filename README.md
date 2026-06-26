# 🌾 Crop Advisor Chatbot – AI-Powered Smart Farming Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg">
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black">
  <img src="https://img.shields.io/badge/Google-Gemini-orange">
  <img src="https://img.shields.io/badge/SQLite-Database-green">
  <img src="https://img.shields.io/badge/License-MIT-red">
</p>

<p align="center">
An intelligent AI-powered agriculture assistant developed using <b>Flask</b>, <b>Google Gemini AI</b>, and <b>SQLite</b>. The chatbot helps farmers and agriculture enthusiasts by providing crop recommendations, fertilizer guidance, plant disease information, weather updates, and multilingual farming support through an easy-to-use web interface.
</p>

---

# 📖 Overview

Crop Advisor Chatbot is a smart agriculture web application that leverages Artificial Intelligence to assist farmers in making better farming decisions.

The chatbot understands natural language queries and provides accurate responses regarding:

- 🌱 Crop recommendations
- 🌦 Weather information
- 🌾 Farming techniques
- 🦠 Plant diseases
- 🧪 Fertilizer recommendations
- 💬 Agriculture-related questions
- 🌍 Multilingual support

The application stores chat history and includes user authentication for personalized experiences.

---

# ✨ Features

## 🤖 AI Chatbot

- Google Gemini powered chatbot
- Natural language understanding
- Intelligent farming advice
- Context-aware conversations

---

## 🌱 Crop Recommendations

- Crop information
- Best cultivation practices
- Soil suitability
- Seasonal recommendations
- Water requirements
- Growth duration

---

## 🌦 Weather Information

- Live weather updates
- City-based weather search
- Temperature
- Humidity
- Weather conditions
- Wind details

---

## 🦠 Disease Information

Provides information about common crop diseases including:

- Symptoms
- Causes
- Prevention
- Treatments
- Best farming practices

---

## 🧪 Fertilizer Guidance

Suggests fertilizers based on crop requirements including:

- Organic fertilizers
- Chemical fertilizers
- Application methods
- Usage recommendations

---

## 🌍 Multilingual Support

Supports multiple languages for better accessibility.

Example:

- English
- Kannada
- Hindi
- Other regional languages

---

## 👤 User Authentication

- User Registration
- Secure Login
- Password Hashing
- Session Management

---

## 💾 Chat History

- Stores conversations
- View previous chats
- Persistent storage using SQLite

---

# 🛠 Technology Stack

## Backend

- Python
- Flask

## AI

- Google Gemini API

## Frontend

- HTML5
- CSS3
- JavaScript

## Database

- SQLite

## Deployment

- Gunicorn
- Render
- PythonAnywhere

---

# 📂 Project Structure

```
crop-advisor-chatbot/
│
├── app.py
├── chatbot.py
├── database.py
├── weather.py
├── requirements.txt
├── Procfile
│
├── data/
│   ├── crops.json
│   ├── diseases.json
│   └── fertilizers.json
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── audio/
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── index.html
│   ├── about.html
│   ├── developer.html
│   └── technology.html
│
└── crop_advisor.db
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/crop-advisor-chatbot.git

cd crop-advisor-chatbot
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux/Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
WEATHER_API_KEY=YOUR_WEATHER_API_KEY
SECRET_KEY=your_secret_key
```

---

# ▶ Run Application

```bash
python app.py
```

Application runs on

```
http://127.0.0.1:5000
```

---

# 🚀 Deployment

The project can be deployed on:

- Render
- Railway
- PythonAnywhere
- VPS
- Azure App Service
- Google Cloud Run

Gunicorn Start Command

```bash
gunicorn app:app
```

---

# 📊 Database

SQLite is used for storing

- User Accounts
- Password Hashes
- Chat History

---

# 📸 Screenshots
<p
<img width="1366" height="633" alt="re" src="https://github.com/user-attachments/assets/eaacb47f-095d-4219-a91a-3707feae1b65" />
  <br>
<img width="1366" height="631" alt="log" src="https://github.com/user-attachments/assets/6128b8b6-db9a-49d5-8e21-916a977b36af" />
  <br>
<img width="1358" height="623" alt="home" src="https://github.com/user-attachments/assets/a4f2638d-b9c6-476f-b4b1-06499751d26f" />
  <br>
<img width="1356" height="624" alt="home2" src="https://github.com/user-attachments/assets/ada834df-c693-49c2-ab47-084714f11c74" />
  <br>
<img width="1351" height="620" alt="home3" src="https://github.com/user-attachments/assets/8bd6eca6-516f-4c6f-a499-97a250d404fa" />
  <br>
<img width="1354" height="633" alt="abo" src="https://github.com/user-attachments/assets/6b34a6bb-e09b-4a4d-83a6-e68a915e0eaf" />
  <br>
<img width="1353" height="631" alt="dev" src="https://github.com/user-attachments/assets/9d48001a-5599-4838-877a-39b2acdceb6c" />
  <br>
<img width="1351" height="628" alt="tech" src="https://github.com/user-attachments/assets/e5359847-0089-499c-8e94-2fc98319a90e" />
  <br>
/p>

# 🔄 Workflow

```
User

↓

Login/Register

↓

Chat Interface

↓

Gemini AI

↓

Agriculture Knowledge

↓

Generate Response

↓

Display Answer

↓

Save Chat History
```

---

# 💡 Future Improvements

- Voice Assistant
- Image-based Disease Detection
- Soil Analysis
- Fertilizer Prediction using ML
- Crop Yield Prediction
- Rainfall Prediction
- GPS Location Support
- Farmer Community Forum
- Mobile Application
- AI Voice Chat
- Offline Mode
- Dashboard Analytics

---

# 🔒 Security

- Password Hashing
- Session Authentication
- Environment Variables
- API Key Protection
- Secure Login
- SQLite Data Storage

---

# 📈 Project Highlights

✔ AI Powered Agriculture Chatbot

✔ Google Gemini Integration

✔ Weather API Integration

✔ SQLite Database

✔ Flask Backend

✔ Responsive UI

✔ User Authentication

✔ Chat History

✔ Crop Information

✔ Disease Information

✔ Fertilizer Recommendations

✔ Multilingual Support

---

# 🎯 Use Cases

- Farmers
- Agriculture Students
- Researchers
- Smart Farming Projects
- College Final Year Projects
- AI Learning Projects

---

# 📚 Learning Outcomes

This project demonstrates practical implementation of:

- Artificial Intelligence
- Large Language Models (LLMs)
- Flask Web Development
- REST APIs
- SQLite Database
- Authentication
- Prompt Engineering
- API Integration
- Session Management
- Full Stack Development

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository

2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📝 License

This project is licensed under the MIT License.

---

# 👨‍💻 Developer

**Prajwal T.S.**

AI & Full Stack Developer

- Python
- Flask
- Machine Learning
- Deep Learning
- Computer Vision
- Generative AI
- Google Gemini
- REST APIs
- SQLite

GitHub:

```
https://github.com/yourusername
```

LinkedIn:

```
https://linkedin.com/in/yourprofile
```

Email:

```
your.email@example.com
```

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.

---

<p align="center">
Made with ❤️ using Python, Flask, SQLite and Google Gemini AI for Smart Agriculture.
</p>

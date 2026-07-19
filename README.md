# 🩺COVID-DISEASE-PREDICTION

A Machine Learning-based web application that predicts whether a patient is **COVID-19 Positive** or **Negative** using clinical health parameters. The application provides an intuitive web interface for users to enter medical information and instantly receive prediction results.

---

## 📌 Overview

The COVID-19 Prediction System is designed to assist in the early screening of COVID-19 cases using machine learning. By analyzing patient health-related input values, the model predicts the likelihood of COVID-19 infection and displays the result through a user-friendly Flask web application.

---

## ✨ Features

- 🩺 COVID-19 Prediction
- 🤖 Machine Learning-Based Classification
- 🔐 User Login & Registration
- 📊 Instant Prediction Results
- 🎨 Responsive User Interface
- ⚡ Fast Prediction
- 💾 SQLite Database for User Management
- 📱 Mobile-Friendly Design

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Joblib

### Database
- SQLite

---

## 📂 Project Structure

```
COVID-19-Prediction-System/
│
├── app.py
├── create_users.py
├── requirements.txt
├── README.md
│
├── dataset/
│   └── COVID19_Prediction_Dataset_Numeric.csv
│
├── db/
│   └── users.db
│
├── model/
│   └── covid.pkl
│
├── static/
│   ├── style.css
│   ├── covid-bg.jpg
│   ├── login-bg.jpg
│   └── result-bg.jpg
│
└── templates/
    ├── index.html
    ├── login.html
    ├── signup.html
    └── result.html
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/COVID-19-Prediction-System.git
```

Navigate to the project folder

```bash
cd COVID-19-Prediction-System
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 📊 Model Workflow

1. User logs into the application.
2. Medical information is entered through the prediction form.
3. The trained machine learning model processes the input.
4. The application predicts:
   - ✅ COVID-19 Positive
   - ❌ COVID-19 Negative
5. The prediction result is displayed instantly.

---

## 🧠 Machine Learning

- Data Preprocessing
- Feature Selection
- Model Training
- Model Serialization using Joblib
- Real-Time Prediction

---

## 📸 Screenshots

> Add screenshots of:

- Login Page
- Sign Up Page
- Prediction Form
- Prediction Result
- Home Page

---

## 🔮 Future Enhancements

- Multi-Disease Prediction
- Doctor Recommendation System
- Hospital Locator
- PDF Report Generation
- User Dashboard
- Prediction History
- Cloud Deployment
- AI-Based Health Suggestions

---

## 👩‍💻 Author

**Sankari R**

Computer Science Engineering Student passionate about Artificial Intelligence, Machine Learning, Data Analytics, and Full Stack Development.


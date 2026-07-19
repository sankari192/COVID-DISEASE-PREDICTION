from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import joblib
import numpy as np
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Load the trained model using joblib
model = joblib.load(os.path.join("model", "covid.pkl"))

# Home route (index page)
@app.route('/')
def home():
    if 'username' in session:
        return render_template('index.html')
    return redirect('/login')


# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])

        db_path = os.path.abspath(os.path.join("db", "users.db"))  # ✅ absolute path
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        if cursor.fetchone():
            return "User already exists. Please login."

        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return redirect('/login')

    return render_template('signup.html')


# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    db_path = os.path.abspath(os.path.join("db", "users.db"))  # ✅ absolute path

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username=?", (username,))
        result = cursor.fetchone()
        conn.close()

        if result and password == result[0]:
            session['username'] = username
            return redirect('/')
        else:
            return 'Invalid credentials. Please try again.'
    return render_template('login.html')


# Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')


# Result route (prediction)
@app.route('/result', methods=['POST'])
def result():
    if 'username' not in session:
        return redirect('/login')

    try:
        input_fields = [
            "Age", "Gender", "Fever", "Cough", "Fatigue", "Headache",
            "Sore_Throat", "Shortness_of_Breath", "Chest_Pain", "Loss_of_Taste",
            "Loss_of_Smell", "Diarrhea", "Diabetes", "Hypertension", "Heart_Disease",
            "Kidney_Disease", "Travel_History", "Contact_With_COVID_Patient",
            "Vaccinated", "Oxygen_Level"
        ]

        features = []
        for field in input_fields:
            value = request.form.get(field)
            if value is None or value == '':
                features.append(0)
            else:
                features.append(float(value))

        prediction = model.predict([np.array(features)])
        result_text = "Positive" if prediction[0] == 1 else "Negative"
        return render_template('result.html', prediction=result_text)
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)

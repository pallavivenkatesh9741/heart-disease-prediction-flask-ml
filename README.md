# Heart Disease Prediction System using Machine Learning

## 📌 Project Overview
The **Heart Disease Prediction System** is a machine learning–based web application developed using **Flask** and a **Random Forest Classifier**.  
It predicts the likelihood of heart disease based on key clinical attributes provided by the user through a web interface.

This project demonstrates an **end-to-end machine learning workflow**, from data preprocessing and model training to deployment as a web application.

---

## 🎯 Objective
The objective of this project is to:
- Predict the presence of heart disease using medical parameters
- Assist in early risk identification
- Showcase practical deployment of ML models using Flask

---

## 🧠 Machine Learning Model
- **Algorithm:** Random Forest Classifier
- **Reason for Selection:**
  - Handles complex feature interactions
  - Reduces overfitting compared to single decision trees
  - Provides robust classification performance

### Model Evaluation Metrics:
- Accuracy Score
- Confusion Matrix
- Classification Report

---

## 📊 Dataset Description
The dataset (`heart.csv`) contains clinical attributes commonly used for heart disease diagnosis.

### Selected Features:
- `age` – Age of the patient
- `cp` – Chest pain type
- `trestbps` – Resting blood pressure
- `chol` – Serum cholesterol level
- `thalach` – Maximum heart rate achieved

### Target Variable:
- `target`  
  - `1` → Presence of heart disease  
  - `0` → No heart disease

---

## ⚙️ Technology Stack
- **Language:** Python
- **Web Framework:** Flask
- **Machine Learning:** Scikit-learn
- **Data Handling:** Pandas
- **Frontend:** HTML (Jinja2 Templates)
- **Model:** Random Forest Classifier

---

## 🏗️ Project Structure
- │
- ├── app.py
- ├── heart.csv
- ├── README.md
- ├── templates/
- │ └── index.html
- └── static/
- └── style.css (optional)

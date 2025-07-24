📊 Sampling-Based Fraud Detection in E-commerce: A Machine Learning Approach
🔍 Overview
This project aims to detect fraudulent transactions in e-commerce platforms using machine learning techniques. We tackled the class imbalance problem often found in fraud datasets using sampling techniques like SMOTE, Random Under Sampling, and SMOTEENN, and trained a Random Forest Classifier for effective prediction.

🚀 Key Features
✅ Preprocessing and cleaning of e-commerce transactional data

🧪 Applied sampling techniques to balance class distribution

🧠 Trained a RandomForestClassifier to detect fraud

📈 Evaluated model using accuracy, precision, recall, and F1-score

🌐 Integrated with Flask to build a web application for real-time prediction

🎨 Designed an interactive HTML/CSS-based frontend for user interaction

📂 Modules
model.py – Data preprocessing, sampling, model training & saving

app.py – Flask backend for prediction and navigation

templates/ – HTML templates for frontend

static/ – CSS styles for UI

fraud_model.joblib – Trained Random Forest model

Label encoders for categorical inputs (product category, payment method)

💻 Technologies Used
Python

Pandas, Scikit-learn, Imbalanced-learn

Flask

HTML, CSS (FontAwesome icons)

Jupyter Notebook (for initial exploration)

📊 Sampling Techniques Used
SMOTE: Synthetic Minority Oversampling

RandomUnderSampler: Reduces majority class

SMOTEENN: Combines SMOTE and Edited Nearest Neighbors for better noise reduction

🧠 Model Evaluation Metrics
Accuracy Score

Precision & Recall

F1-Score

Confusion Matrix

📷 Frontend
Designed with HTML & CSS

5 Navigation Buttons (Introduction, Team, Dataset, Prediction, Project Report)

FontAwesome icons for improved UI/UX



📌 How to Run
bash
Copy
Edit
1. Clone this repository
2. Install dependencies using pip
3. Run `app.py` to start the Flask server
4. Open the browser and navigate to http://localhost:5000

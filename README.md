# Phishing-link-detector-using-ML
A machine learning–based system designed to detect whether a given URL is legitimate or phishing. This project helps users stay safe from online scams, credential theft, and cyber-attacks by automatically analyzing URL features and predicting their authenticity.
Project Overview

Phishing attacks are increasing rapidly, and most users cannot easily identify fake URLs.
This project uses URL-based features and ML algorithms to classify links as safe or malicious.

The system extracts key characteristics from URLs, processes them using machine learning models, and returns a prediction with high accuracy.

---------------------🎯 Features--------------------------------

Classifies URLs as “Legitimate” or “Phishing”

Extracts important URL features like:

URL length

Special character count

Presence of HTTPS

Domain age

IP address in URL

Uses multiple ML algorithms for comparison

Achieves high accuracy

Scalable and easy to integrate into browsers or security tools

-----------------------🧠 Machine Learning Models Used---------------------------

Logistic Regression

Random Forest Classifier

Support Vector Machine (SVM)

These models are chosen for their strong performance in classification problems.

---------------------------🗂️ Dataset-----------------------------------------------

Dataset sourced from:

Kaggle / UCI Machine Learning Repository

Contains:

Thousands of phishing and legitimate URLs

Balanced classes for unbiased model training

Extracted URL features stored in CSV format

---------------------------🏗️ How It Works------------------------------------------

Collect URL Dataset

Extract Features from each URL

Preprocess the Data

Train ML models using Scikit-learn

Evaluate accuracy

Predict new URLs

-----------------------------🛠️ Tech Stack---------------------------------------------

Python

Pandas

NumPy

Scikit-learn

Matplotlib / Seaborn (optional for graphs)

VS Code / Jupyter Notebook

📊 Results

The model shows high accuracy in classifying phishing and safe URLs, making it useful for real-world cybersecurity applications.

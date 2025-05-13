# Trasliterated Bengali Bullying Comment Detection

## Table of Contents
1. [Description](#description)
2. [Technology Stack](#technology-stack)
3. [Prerequisites](#prerequisites)
4. [Usage](#usage)
6. [Conclusion](#conclusion)




---

## Description
This project focuses on detecting transliterated Bengali bullying comments from social media platforms like Facebook and YouTube. The collected comments are processed to extract linguistic and contextual features, which are then transformed and fed into multiple machine learning models. The goal is to identify the best-performing model for accurately classifying bullying content in transliterated Bengali (Bengali written in Latin script).

Key steps include:

* Data Collection: Gathering transliterated Bengali comments from social media.

* Text Processing: Cleaning, normalizing, and extracting features from the raw text.

* Model Training: Evaluating different ML models to determine the most effective classifier.

* Deployment: (Optional) Integrating the best model into a usable system for real-time detection.

This work contributes to mitigating online harassment by automating the detection of abusive content in non-native script formats.


## Technology Stack

### Core Components
- **Language**: Python 3
- **Local Interface**: Flask 

### Text Processing Pipeline

- **Regex Processing**: Python's `re` module for text cleaning
- **Sentiment Analysis**: Word-counting using custom positive/negative word lists
- **Feature Extraction**: TF-IDF (`TfidfVectorizer`) applied only to text content

### Machine Learning Models
- **Algorithms Tested**:
  - Random Forest
  - Support Vector Machine (SVM)
  - K-Nearest Neighbors (KNN)
  - Naive Bayes
- **Implementation**: All models from `sklearn`

### Output Visualization
- **Simple Web Interface**: Flask-rendered HTML showing:
  - Input comment
  - Sentiment analysis results
  - Model predictions



## Prerequisites

Be sure you have the following installed on your development machine:

- Python 3.12
- Flask
- Git
- pip
- Virtualenv


## Usage
```bash
git clone [repo-url]
pip3 install -r "requirements.txt"

python3 src/components/data_ingestion.py
python3 app.py    # run the application locally

```

## Conclusion
After evaluating multiple machine learning models (Random Forest, SVM, KNN, and Naive Bayes) for detecting transliterated Bengali bullying comments, Naive Bayes achieved the highest accuracy of 69.9% on our dataset. 


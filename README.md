# Trasliterated Bengali Bullying Comment Detection

## Table of Contents
1. [Description](#description)
2. [Technology Stack](#technology Stack)
3. [Dataset](#dataset)
4. [Models](#models)
5. [Result](#result)
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




## Dataset




## Result

naive bayes

## Conclusion
rew o

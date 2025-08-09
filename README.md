# Movie Recommendation System (Content-Based) using Machine Learning

## 📌 Overview
This project is a Content-Based Movie Recommendation System that suggests similar movies based on the content (genres, cast, keywords, and descriptions) of a given movie. It is built with Python, Pandas, and scikit-learn, and deployed using Streamlit.

## 🚀 Features
- Suggests top 5 similar movies for a given title
- Uses cosine similarity on vectorized movie metadata
- Simple and interactive UI built with Streamlit

## 🛠 Technologies Used
- Programming Language: Python
- Tools & Libraries: Streamlit, requests, numpy, pandas, nltk, PorterStemmer, CountVectorizer, os, ast, nltk , PorterStemmer, from sklearn.feature_extraction.text import CountVectorizer, from sklearn.metrics.pairwise import cosine_similarity, and pickle.
- IDE: JupyterNotebook
- Prerequisites: Python, Machine Learning

## 📂 Dataset
This Dataset is taken from the Kaggle open source platform.
In this project I uses the TMDB dataset:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

## ⚙️ PROPOSED METHODOLOGY/ SYSTEM ARCHITECTURE
The proposed movie recommendation system using machine learning is based on the content-based recommendation. It involves several key steps and methodologies. Here’s general methodology as follows:
1. Data collection : A very first step is gathering dataset containing information about movies. This dataset should include features like movie title, genre, director, actors, etc. for that we collect dataset from the online website called Kaggle named “IMDb 5000 movies” dataset which contain the two CSV files movies.csv and credits.csv. IMDb or similar databases are used.
2. Data Preprocessing : clean the dataset by handling missing values, removing duplicates, and standardizing formats. Dataset which we select consists of various attributes are in the form of list of dictionary and we converted into the list format so that it will easy for the further analysis. Removing the space in between the words using transformation, common words, droping unnecessary attribute, fetching, merging the attributes, etc.
3. Feature Extraction : we use the CountVectorizer library for extracting the unique text from the list such as “English” words which results in matrix, often referred to as “document-term matrix” or “bag-of-words” representation.
4. Building the Recommendation Model:
4.1. Content Representation: Combine the feature extracted from unique text feature to create the unified representation of each movie.
4.2. Calculation of Similarity: Using the cosine similarity we measures to calculate the similarity between the movies based on their feature representations.
5. Model Evaluation: Evaluate the performance of the recommendation system using metrics such as precision, recall, F1-score, cross- validation techniques can be used to ensure robustness.
6. Deployment : Once the model is evaluated, we deploy it in production environment for that we use streamlit function of python. It involves the integration of files into a web application

## Results
<img width="1020" height="757" alt="Screenshot 2025-08-09 130254" src="https://github.com/user-attachments/assets/278c1e37-0931-4adc-8495-e67e2635bf25" />
<img width="955" height="723" alt="Screenshot 2025-08-09 130526" src="https://github.com/user-attachments/assets/070ce989-0454-45a1-aa66-3f94fa950315" />

## Conclusion
- In conclusion, a movie recommendation system leverages various techniques and algorithms to provide personalized suggestions to users based on their preferences, historical data, and similarity metrics. By analyzing user interactions, ratings, and content features, recommendation systems can effectively predict and recommend movies that align with individual tastes and preferences.

## Command to Run the code
<img width="829" height="150" alt="Screenshot 2025-08-09 130812" src="https://github.com/user-attachments/assets/44387c98-83da-472d-8688-e8785caa5c8a" />

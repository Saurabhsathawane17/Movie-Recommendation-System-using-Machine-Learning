import pickle
import streamlit as st
import requests
import pandas as pd

# Function to fetch movie poster from OMDb API
def fetch_poster(movie_title):
    api_key = "5abf82e6"  # OMDb API key
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    if data.get('Poster') and data['Poster'] != 'N/A':
        return data['Poster']
    else:
        return "https://via.placeholder.com/300x450?text=No+Image"



# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_title = movies.iloc[i[0]].title
        recommended_movie_names.append(movie_title)
        recommended_movie_posters.append(fetch_poster(movie_title))
    return recommended_movie_names, recommended_movie_posters

# Load data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit UI
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom right, #2e004f, #000000);
    font-family: 'Arial', sans-serif;
    color: white;
    text-align: center;
}
.hero {
    padding-top: 80px;
}
.hero-title {
    font-size: 3rem;
    font-weight: bold;
}
.hero-title .yellow {
    color: #FFD700;
}
.hero-title .blue {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.subtitle {
    font-size: 1.2rem;
    color: #ccc;
    margin-top: 10px;
}
.features {
    display: flex;
    justify-content: center;
    gap: 30px;
    margin-top: 20px;
}
.feature {
    font-size: 1rem;
    display: flex;
    align-items: center;
    gap: 8px;
}
.search-container {
    margin-top: 30px;
    display: flex;
    justify-content: center;
}
.search-input {
    padding: 15px;
    border-radius: 50px 0 0 50px;
    border: none;
    outline: none;
    width: 400px;
    font-size: 1rem;
    background: #111;
    color: white;
}
.search-button {
    padding: 15px 25px;
    border: none;
    border-radius: 0 50px 50px 0;
    background: linear-gradient(90deg, #FFD700, #ffae42);
    font-weight: bold;
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)


# Hero Section
st.markdown("""
<div class="hero">
    <div class="hero-title">
        <span class="yellow">Movie</span> <span class="blue">Recommendation</span> <span style="color: white;">System</span>
    </div>
    <div class="subtitle">
        Discover your next favorite movie with our AI-powered recommendation system
    </div>
    <div class="features">
        <div class="feature">⚡ AI Powered</div>
        <div class="feature">📦 Personalized</div>
        <div class="feature">⚡ Instant Results</div>
    </div>
</div>
""", unsafe_allow_html=True)

selected_movie_name = st.selectbox(
    "Search for a movie:",
    movies['title'].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.image(poster, use_container_width=True)
            st.markdown(f"**{name}**")

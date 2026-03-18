# Movie Recommender System 🎬

[View Movie Recommender System](https://movierecommendersystem-3mwpnnrwcxlph9wavxwhob.streamlit.app/)

## Overview

The Movie Recommender System is a web application built using Streamlit. It recommends movies based on user input using a similarity matrix derived from movie features. The app allows users to select a movie from a dropdown menu and displays a list of recommended movies along with their posters.

## Features

- **Movie Recommendations:** 🎥 Provides a list of recommended movies based on the selected movie.
- **Movie Posters:** 🖼️ Displays movie posters for recommended movies.

## Technologies Used

- **Python:** 🐍 Programming language used for developing the app.
- **Streamlit:** 🌐 Framework used for building the interactive web application.
- **Pandas:** 📊 Library used for data manipulation and analysis.
- **Requests:** 📡 Library used for making HTTP requests to fetch movie posters.
- **Gdown:** ⬇️ Library used for downloading files from Google Drive.
- **Pickle:** 💾 Python library used for serializing and deserializing objects.
- **Scikit-learn:** ⚙️ Library used for machine learning, specifically for feature extraction and similarity computation.
- **NLTK:** 📚 Library used for natural language processing, specifically for stemming.

## How It Works

### Data Preprocessing and Model Building

1. **Data Loading:**
   - Load movie data and credits from CSV files.
   - Merge the datasets on movie titles to consolidate information.
   - Retain only the relevant columns: `movie_id`, `title`, `overview`, `genres`, `keywords`, `cast`, and `crew`.

2. **Data Cleaning:**
   - Handle missing values by dropping rows with null entries.
   - Convert JSON-like structures in columns (e.g., `genres`, `keywords`, `cast`, `crew`) to lists of relevant attributes.
   - Extract specific information such as genre names, keywords, and cast members for further processing.

3. **Feature Engineering:**
   - Combine multiple columns (`overview`, `genres`, `keywords`, `cast`, `crew`) into a single `tags` column to create a unified text representation of each movie.
   - Preprocess the text data by:
     - Converting it to lowercase for uniformity.
     - Applying stemming to reduce words to their base forms (e.g., "loved", "loving", and "love" become "love").

4. **Model Building:**
   - Use `CountVectorizer` to convert the processed text data into feature vectors.
   - Compute cosine similarity between these vectors to create a similarity matrix that captures the relationships between movies.

5. **Recommendation Function:**
   - Define a function to recommend movies based on a selected movie title using the similarity matrix.
   - Fetch the top 5 most similar movies and their respective posters.

6. **Pickle Files:**
   - Save the processed movie data and similarity matrix as pickle files (`movie_dict.pkl` and `similarity.pkl`) for efficient loading in the Streamlit app.

## Configuration

You can configure the app by updating the following variables in the script:

- **Download Similarity Matrix:** This link provides the `similarity.pkl` file required by the app. [Download Link](https://drive.google.com/uc?id=1nRxFIkLs-lfRtUVozJCUAEssNkiigzd8)
- Update the `api_key` in the `fetch_poster` function with your own TMDB API key if needed to fetch movie posters.

## View the App

You can view the live Movie Recommender System app by clicking on the link below:

[View Movie Recommender System](https://movierecommendersystem-3mwpnnrwcxlph9wavxwhob.streamlit.app/)

## Contact

For any questions, suggestions, or feedback, please feel free to reach out:

- **Aditya Pathak** 👤
- **Email:** [adityapathak034@gmail.com](mailto:adityapathak034@gmail.com) 📧
- **GitHub:** [adityapathak0007](https://github.com/adityapathak0007) 🐙
- **LinkedIn:** [adityapathak07](https://www.linkedin.com/in/adityapathak07) 🔗

### Install Dependencies

Clone the repository and install the required packages:

```bash
git clone https://github.com/adityapathak0007/MovieRecommenderSystem.git
cd MovieRecommenderSystem
pip install -r requirements.txt

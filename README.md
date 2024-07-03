# Movie Recommendation System

This project implements a simple movie recommendation system using natural language processing (NLP) techniques and machine learning. It uses the TMDb 5000 Movies and TMDb 5000 Credits datasets to generate recommendations based on movie tags.

## Overview

The system processes movie metadata to create a comprehensive set of tags for each movie. These tags are then vectorized and used to calculate cosine similarity between movies. Based on this similarity, the system can recommend movies that are most similar to a given movie.

## Features

- Merges movie and credits data on the movie title.
- Processes data to extract relevant information: genres, keywords, cast, crew, and overview.
- Creates a unified set of tags for each movie.
- Uses NLP techniques to stem the tags.
- Calculates cosine similarity between movie vectors.
- Recommends movies based on similarity scores.

## Installation

1. Clone the repository:
    ```bash
    https://github.com/irvincardoza/movie-recommendation-system.git
    ```

2. Set up a virtual environment and install dependencies:
    

3. Ensure you have the necessary NLTK data:
    ```python
    import nltk
    nltk.download('stopwords')
    ```

## Usage

Run the script to generate recommendations:
```python
python movie.py
```

## Web Application
- To be available soon

# Playlist Song Recommendation System

A music recommendation system that suggests similar songs based on playlist data using Word2Vec embeddings.

## Table of Contents
- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Example](#example)

## Project Description
This recommendation system uses Word2Vec machine learning techniques to analyze playlist patterns and recommend songs that frequently appear together in user-generated playlists. The system trains on playlist data and song metadata to generate contextual recommendations.

Key features:
- Trains a Word2Vec model on playlist sequences
- Processes playlist data containing 10,000+ songs
- Provides top 5 recommendations for any given song
- Displays song title and artist information
- Uses vector embeddings to capture musical context

## Installation

### Requirements
- Python 3.6+
- Required packages:
  ```bash
  pip install gensim pandas numpy
  ```
### Usage
- Run the recommendation.py file
- 2. Get recommendations
  Modify the song ID in the print_recommendations() function call to get different recommendations:
  ``` bash
  print(print_recommendations(1234))  # Replace with your target song ID
  ```
### Data Sources
- Playlist data: train.txt from Google Cloud Storage
- Song metadata: song_hash.txt from Google Cloud Storage
- Both files are automatically fetched during execution

### Example
- Sample Input
``` bash
print(print_recommendations(2172))
```
- Expected output
``` bash
Song Info: 
Title: Hey Jude
Artist: The Beatles

Recommended Songs are 
                    title          artist
id                                       
1234         Let It Be      The Beatles
5678         Yesterday     The Beatles
9012       Come Together  The Beatles
3456         Imagine      John Lennon
7890   Bohemian Rhapsody          Queen
```

  

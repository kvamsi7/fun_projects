import gensim.downloader as api
from gensim.models import Word2Vec
import pandas as pd 
from urllib import request
import numpy as np

# load glove embedding model
# embed_model = api.load("glove-wiki-gigaword-50")

# print(embed_model.most_similar([embed_model['king']],topn=11))

# Get the playlist dataset file
data = request.urlopen('https://storage.googleapis.com/maps-premium/dataset/yes_complete/train.txt')

# Parse the palylist dataset file. skip the first two lines as they contain metadata
lines = data.read().decode('utf-8').split('\n')[2:]

# Remove playlist with only one song
playlists = [playlist.rstrip().split() for playlist in lines if len(playlist.split()) > 1]

# load song metadata
songs_file = request.urlopen('https://storage.googleapis.com/maps-premium/dataset/yes_complete/song_hash.txt')
songs_file = songs_file.read().decode('utf-8').split('\n')
songs = [s.rstrip().split('\t') for s in songs_file]
songs_df = pd.DataFrame(data=songs, columns = ['id','title','artist'])
songs_df = songs_df.set_index("id")

# print('Playlist $1:\n',playlists[0],'\n')

model = Word2Vec(
    playlists, vector_size = 32, window = 20, negative = 50, min_count = 1, workers = 4
)

# print('Example 1')
# song_id = 2172
# print(model.wv.most_similar(positive = str(song_id)))


def print_recommendations(song_id):
    song_info = songs_df.iloc[song_id]
    print("\nSong Info: ")
    print("Title : ",song_info.title)
    print("Artist :", song_info.artist)

    print("\nRecommended Songs are ")
    similar_songs = np.array(model.wv.most_similar(positive = str(song_id), topn =5 ))[:,0]
    return songs_df.iloc[similar_songs]

print(print_recommendations(2172))

print(print_recommendations(842))


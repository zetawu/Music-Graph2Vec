# README

This is the code for the paper "Music-Graph2Vec: An Efficient Method for Embedding Pitch Segment". The main focus of this code is to train pitch segment embeddings and perform genre classification based on these embeddings.

The three Python scripts have the following functions:

* `dataset_segment.py`: randomly extracts a subset from the music dataset with a specified size.
* `genre_classification.py`: calculates the average of the pitch segment vectors for each song to obtain a single vector for each song, and then uses KNN for classification.
* `train_Music-Graph2Vec.py`: trains pitch segment embeddings using Music-Graph2Vec.

The "trained" directory stores our three trained pitch segment embeddings in key-value pairs.

### Requirements

The codebase is implemented in Python 3.8 package versions.

`pip install -r requirements.txt`


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

### Citation

If you use this code in your research, please cite:

```bibtex
@inproceedings{10.1145/3595916.3626740,
author = {Wu, Taiwei and Zhang, Jianhao and Duan, Lian and Cai, Yuanzhe},
title = {Music-Graph2Vec: An Efficient Method for Embedding Pitch Segment},
year = {2024},
isbn = {9798400702051},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3595916.3626740},
doi = {10.1145/3595916.3626740},
abstract = {Learning low-dimensional continuous vector representation for short pitch segment extracted from songs is has been confirmed to contain tonal features of music, which is key to melody modeling that can be utilized in many music investigations, such as genre classification, emotion classification, and music retrieval, and so on. The skip-gram version of&nbsp;Word2Vec&nbsp;is ubiquitous, and widely used approach for music pitch segment embedding, but it poorly scales to large data sets due to its extremely long training time. In this paper, we propose a novel efficient graph-based embedding method, named&nbsp;Music-Graph2Vec, to tackle this concern. This approach converts music files into graphs, extracts the rhythmic sequence through random walking, and trains the rhythmic embedding model using skip-gram. Experimental results demonstrate that&nbsp;Music-Graph2Vec&nbsp;outperforms&nbsp;Word2Vec&nbsp;in training rhythmic embedding, with the advantage of being 55 times faster on the top-MAGD dataset (2,134.7s for&nbsp;Word2Vec&nbsp;and 38.9s for&nbsp;Music-Graph2Vec), with the same accuracy for&nbsp;Word2Vec&nbsp;in terms of music genre classification.},
booktitle = {Proceedings of the 5th ACM International Conference on Multimedia in Asia},
articleno = {97},
numpages = {5},
keywords = {Embedding, Genre Classification, MIDI, Music Graph, Random Walk},
location = {Tainan, Taiwan},
series = {MMAsia '23}
}
```


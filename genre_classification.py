# Take the average of the pitch segment vectors for each song to obtain a single vector for each song, and then use KNN for classification.
# The pitch segments for each genre should be placed in the current directory as separate files, with the filename being the name of the genre, such as "classical.txt".
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import os
from gensim import models


def read_data(filename):
    result = []
    with open(filename, 'r') as file:
        for line in file:
            row = line.strip().split()
            result.append(row)
    return result


def getmean(a):
    # Initialize a list of length 256 to store the sum of elements at each position
    sum_list = [0] * 128

    # Traverse each sublist and add up the elements at each position
    for sublist in a:
        for i in range(128):
            sum_list[i] += sublist[i]

    # Divide the sum of elements at each position by the number of sublists to obtain the average at each position
    return [x / len(a) for x in sum_list]


txt_files = [f for f in os.listdir() if f.endswith('.txt')]
genres = [os.path.splitext(f)[0] for f in txt_files]
lables = []
adv = []
# Load the trained model, noted that the model should be stored as key-value pairs
trained_model = models.KeyedVectors.load_word2vec_format('your trained model dir')
for genre in genres:
    # load data
    slices = read_data('./' + genre + '.txt')
    for r in slices:
        genre_vecs_advanced = []
        for i in r:
            if i in trained_model:
                genre_vecs_advanced.append(trained_model[i])
        genre_vecs_advanced = getmean(genre_vecs_advanced)
        lables.append(genre)
        adv.append(genre_vecs_advanced)
# classify with KNN
clf = KNeighborsClassifier(7)
scores = cross_val_score(clf, adv, lables, cv=10, n_jobs=10)
print("acc:", scores.mean())

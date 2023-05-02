# Train pitch segment embeddings using Music-Graph2Vec
# The pitch segment corpus should be placed in a single file and placed in the current directory.
# The pitch segments within the file should be separated by spaces, with each line representing a single song.
import os
import psutil
import time


def read_data(filename):
    result = []
    with open(filename, 'r') as file:
        for line in file:
            row = line.strip().split()
            result.append(row)
    return result


def split_word(raw):
    sents = raw.split(' ')
    return sents


# Text preprocessing
strline = []
with open(r"your_pitch_segment_corpus_dir", encoding='utf-8') as f:
    for line in f:
        strline.extend(split_word(line))  # Split words by space

# Count word frequency
data = {}
min_data = {}
for i in range(0, len(strline) - 1):
    min_data[strline[i]] = min_data.get(strline[i], 0) + 1

# Count co-occurrence frequency of two words and create key-value pairs in the dictionary
for i in range(0, len(strline) - 1):
    if min_data[strline[i]] > 1 and min_data[strline[i + 1]] > 1 and strline[i] != '\n' and strline[i + 1] != '\n':
        data[(strline[i], strline[i + 1])] = data.get((strline[i], strline[i + 1]), 0) + 1

# Generate word graph, if there is no edge file, generate it automatically
with open(r"./pitch_segments.edge", 'w', encoding='utf-8') as f:
    for phrase, fre in data.items():
        line = str(phrase[0]) + ' ' + str(phrase[1]) + ' ' + str(fre) + '\n'
        f.write(line)

# Specify parameters needed to train word embeddings using pecanpy
p = 1
q = 0.001
walklenth = 100
numwalks = 30
dims = 128
time0 = time.perf_counter()
# Train embeddings using pecanpy and store the results in ./pitch_segments.emb in the form of key-value pairs
tppp = 'pecanpy --input "./pitch_segments.edge" --output "./pitch_segments.emb" --mode SparseOTF  --verbose --weighted --directed --p ' + str(
    p) + ' --q ' + str(q) + ' --walk-length ' + str(walklenth) + ' --num-walks ' + str(
    numwalks) + ' --dimensions ' + str(dims)
os.system(tppp)
print("time:", time.perf_counter() - time0)
print('memory: %.4f GB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024 / 1024))

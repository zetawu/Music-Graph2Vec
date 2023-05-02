# randomly extract a subset from the music dataset with a specified size
import random
import os

# specify subset sizes (in bytes)
subset_sizes = [1024, 10240, 102400, 1048576, 10485760, 20971520, 41943040]

# read all lines from the txt file
with open('your_pitch_segment_corpus_dir', 'r') as f:
    lines = f.readlines()

# randomly select lines to form subsets with size close to the specified size
for size in subset_sizes:
    subset = []
    subset_size = 0
    while subset_size < size:
        line = random.choice(lines)
        subset.append(line)
        subset_size += len(line)
    # write the subset to a file
    if size < 1024:
        filename = f'subset_{size}B.txt'
    elif size < 1024 * 1024:
        filename = f'subset_{size // 1024}KB.txt'
    elif size < 1024 * 1024 * 10:
        filename = f'subset_{size // 1024 // 1024}MB.txt'
    else:
        filename = f'subset_{size // 1024 // 1024}MB.txt'
    with open(filename, 'w') as f:
        f.writelines(subset)
    # check if the size of the subset meets the requirement
    actual_size = os.path.getsize(filename)
    if abs(actual_size - size) > 1024:
        print(f'Warning: actual size of {filename} is {actual_size}, expected size is {size}.')

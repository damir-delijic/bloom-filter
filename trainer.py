import math
from bitarray import bitarray


def calculate_k(corpus_size, bloom_size):
    k = math.ceil((bloom_size/corpus_size) * math.log(2))
    if k > 50:
        k = 50
    return k

def count_dataset_dimensions(filename):
    file = open(filename, 'r')

    line = file.readline()
    if not line:
        return 0, 0
    
    shingles_num = 1
    corpus_size = len(line.replace('\n', '').split(','))

    while True:
        # Get next line from file
        line = file.readline()
        if not line:
            break
        shingles_num += 1

    file.close()

    return corpus_size, shingles_num

def get_seeds(k):
    prime_seeds = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229]
    return prime_seeds[0 : k]

def initialize_signature_vector(corpus_size, fake_infinity):
    return [fake_infinity for _ in range(corpus_size)]

def row_permutation(r, seed, modulator):
    return (seed * (r + 1) + 1) % modulator

def update_vector_signatures(vector, seed, row, row_num, modulator):
    r = row_num
    r_p = row_permutation(r=r, seed=seed, modulator=modulator)

    for c in range(len(row)):
        if row[c] == '0' or row[c] == 0:
            pass
        else:
           if r_p < vector[c]:
                vector[c] = r_p

def save_bloom(bloom, seed, filename, is_first, is_last):
    read_mode = ""
    if is_first:
        read_mode = "w"
    else:
        read_mode = "a"

    with open(filename, read_mode) as myfile:
        myfile.write(str(seed))
        myfile.write('\n')
        for i in range(len(bloom)):
                myfile.write(str(bloom[i]))
        if not is_last:
            myfile.write('\n')
            myfile.write('\n')

def train(filename, model_path):

    corpus_size, shingles_num = count_dataset_dimensions(filename=filename)

    bloom_size = shingles_num

    k = calculate_k(corpus_size=corpus_size, bloom_size=bloom_size)

    seeds = get_seeds(k)
  
    for i in range(k):
        
        bloom = bloom_size * bitarray('0')
        vector = initialize_signature_vector(corpus_size=corpus_size, fake_infinity=shingles_num)
        seed = seeds[i]
        # cita iz fajla liniju po liniju i racuna potpise
        file = open(filename, 'r')
        count = 0
    
        max_r = shingles_num

        while True:
            # Get next line from file
            line = file.readline()
            if not line:
                break

            row = line.replace('\n', '').split(',')
            
            update_vector_signatures(vector=vector, seed=seed, row=row, row_num=count, modulator=max_r)
            count += 1

        file.close()

        for j in range(len(vector)):
                position = vector[j]
                if position < max_r:
                    bloom[position] = 1

        is_first = i == 0
        is_last = i == k - 1
        save_bloom(bloom=bloom, seed=seed, filename=model_path, is_first=is_first, is_last=is_last)



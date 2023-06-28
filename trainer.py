from bitarray import bitarray
import random

def permute_row(r, seed, modulator):
    return (seed * r + 1) % modulator

def calculate_characteristic_matrix_dimensions(input_path):
    filename = input_path

    file = open(filename, 'r')

    line = file.readline()
    if not line:
        return 0, 0
    
    shingles_num = 1
    docs_num = len(line.replace('\n', '').split(','))

    while True:
        # Get next line from file
        line = file.readline()
        if not line:
            break
        shingles_num += 1

    file.close()
    return docs_num, shingles_num

def generate_seeds(count, seed_value_limit):
    seeds = []
    for i in range(count):
        random_seed = random.randint(1, seed_value_limit)
        isKnown = False
        for j in range(len(seeds)):
            if seeds[j] == random_seed:
                isKnown = True
                break
        
        while isKnown:
            random_seed = random.randint(1, seed_value_limit)
            isKnown = False
            for j in range(len(seeds)):
                if seeds[j] == random_seed:
                    isKnown = True
        
        seeds.append(random_seed)
    return seeds

def initialize_signature_matrix(docs_num, permutations_num, fake_infinity):
    return [[ fake_infinity for __ in range(docs_num)] for _ in range(permutations_num)]

def handle_row(sig_mat, row, seeds, r, modulator):
    row_permutations = []
    for seed in seeds:
        h = permute_row(r=r, seed=seed, modulator=modulator)
        row_permutations.append(h)

    for c in range(len(row)):
        if row[c] == 0 or row[c] == "0":
            pass
        else:
            for i in range(len(row_permutations)):
                if sig_mat[i][c] > row_permutations[i] :
                    sig_mat[i][c] = row_permutations[i]

def compute_singature_matrix(input_path, seeds, docs_num, shingles_num):
    # broj singlova treba da bude prost, dodati k redova nula
    sig_mat = initialize_signature_matrix(docs_num=docs_num, permutations_num=len(seeds), fake_infinity=shingles_num)

    filename = input_path

    file = open(filename, 'r')
    count = 0
    while True:
        # Get next line from file
        line = file.readline()
        if not line:
            break

        row = line.replace('\n', '').split(',')
        
        handle_row(sig_mat=sig_mat, row=row, seeds=seeds, r=count, modulator=(shingles_num))
        count += 1

    file.close()

    return sig_mat

def banding(sig_mat, b, r, docs_num, prime_factor):
    bands_mat = []
    for i in range(b):
        temp = handle_band(sub_mat=sig_mat[i*r: (i+1)*r], band_id=i+1, docs_num=docs_num, prime_factor=prime_factor)
        bands_mat.append(temp)
    return bands_mat

def hash_vector(vector, prime_factor):
    q = 433494437
    result = 0
    for i in range(len(vector)):
        num = vector[i]
        result = (result + (pow(q, i)*num) % prime_factor) % prime_factor
    return result

def handle_band(sub_mat, band_id, docs_num, prime_factor):
    result = []
    for c in range(docs_num):
        doc = [band_id]
        for i in range(len(sub_mat)):
            doc.append(sub_mat[i][c])
        temp = hash_vector(doc, prime_factor)
        result.append(temp)
    return result
        
def compute_bloom(bands_mat, bloom_size):
    bloom = bitarray(bloom_size)
    for band in bands_mat:
        for hash_value in band:
            bloom[hash_value] = 1

    return bloom

def train(input_path, permutations_num, b, r, bloom_size):
    # bloom size i broj shinglova da budu prosti brojevi
    # broj permutacija da bude jedna b puta r
    print('started training son')
    docs_num, shingles_num = calculate_characteristic_matrix_dimensions(input_path)
    seeds = generate_seeds(count=permutations_num, seed_value_limit=permutations_num * 10)
    sig_mat = compute_singature_matrix(input_path=input_path, seeds=seeds, docs_num=docs_num, shingles_num=shingles_num)
    bands_mat = banding(sig_mat=sig_mat, b=b, r=r, docs_num=docs_num, prime_factor=bloom_size)
    bloom = compute_bloom(bands_mat=bands_mat, bloom_size=bloom_size)
    save_bloom(bloom, seeds, 'model/bloom.txt')
    print("all done son")

def save_bloom(bloom, seeds, filename):

    with open(filename, "w") as myfile:
        myfile.write(" ".join(str(seed) for seed in seeds))
        myfile.write('\n')
        for i in range(len(bloom)):
                myfile.write(str(bloom[i]))

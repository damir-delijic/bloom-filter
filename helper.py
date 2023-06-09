import random
from bitarray import bitarray
import math
import hashlib


def generate_seeds(number_of_seeds):
    result = []
    start = 3
    end  = 7
    for i in range(0, number_of_seeds):
        random_seed = random.randint(start, end) # pokriva sve indekse redova
        result.append(random_seed)
        start = end + 1
        end = 2 * end + 1
    return result

def initialize_signature_matrix(number_of_documents, number_of_hash_functions, infinity):
    return [[infinity for _ in range(number_of_documents)] for _ in range(number_of_hash_functions)]

def initialize_bloom_filter(m):
    return bitarray(m)

def calculate_number_of_hash_functions(number_of_documents, bloom_filter_size):
    return math.floor((bloom_filter_size/number_of_documents) * math.log(2)) # broj permutacija / hes funkcija

def hash_with_seed(row_number, seed, number_of_shingles):
    return (seed * row_number + seed) % number_of_shingles

def update_signatures(signatures, seeds, row, row_num, number_of_shingles):
   

    r = row_num
    row_hashes = []
    for i in range(len(seeds)):
        row_hashes.append(hash_with_seed(r, seeds[i], number_of_shingles))
    row = row.replace('\n', '')
    vector = row.split(',')

    for column in range(len(vector)):
        if vector[column] == '0':
            pass
        else:
            for j in range(len(signatures)):
                if row_hashes[j] < signatures[j][column]:
                    signatures[j][column] = row_hashes[j]


def old_hash_with_seed(data, seed, modulator):
    # Concatenate the seed with the data
    data_with_seed = seed + data

    #encode
    data_with_seed = data_with_seed.encode('ASCII')

    # Create a hash object using the desired algorithm (e.g., SHA-256)
    hash_object = hashlib.sha256(data_with_seed)

    # Hash digest

    digest = hash_object.hexdigest()

    # hex to decimal

    decimal = int(digest, 16)

    # modulated

    modulated = decimal % modulator

    return modulated
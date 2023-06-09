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

def initialize_signature_vector(number_of_documents, infinity):
    return [infinity - 1 for _ in range(number_of_documents)]

def initialize_bloom_filter(m):
    return bitarray(m)

def calculate_number_of_hash_functions(number_of_documents, bloom_filter_size):
    return math.ceil((bloom_filter_size/number_of_documents) * math.log(2)) # broj permutacija / hes funkcija

def hash_with_seed(row_number, seed, number_of_shingles):
    return (seed * (row_number + 1) + seed) % number_of_shingles

def update_vector_signatures(signatures, seed, vector, row_num, number_of_shingles):
    r = row_num
    row_hash = hash_with_seed(r, seed, number_of_shingles)

    for column in range(len(vector)):
        if vector[column] == '0' or vector[column] == 0:
            pass
        else:
           if row_hash < signatures[column]:
                signatures[column] = row_hash

def update_signatures(signatures, seeds, row, row_num, number_of_shingles):
    r = row_num
    row_hashes = []
    for i in range(len(seeds)):
        row_hashes.append(hash_with_seed(r, seeds[i], number_of_shingles))
   
    vector = row

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


def save_bloom_filter(bitarray, seed, filename, isFirst, isLast):
    readMode = ""
    if isFirst:
        readMode = "w"
    else:
        readMode = "a"

    with open(filename, readMode) as myfile:
        myfile.write(str(seed))
        myfile.write('\n')
        for i in range(len(bitarray)):
                myfile.write(str(bitarray[i]))
        if not isLast:
            myfile.write('\n')
            myfile.write('\n')

def save_parameters_necessary_for_detection(max_value, seeds, filename):
     with open(filename, "w") as myfile:
        myfile.write(str(max_value))
        myfile.write('\n')
        seed_str = ''
        for i in range(len(seeds)):
            seed_str += (str(seeds[i]))
            if i == len(seeds) - 1:
                pass
            else:
                seed_str += ','
        myfile.write(seed_str)
                
def read_detection_parameters(filename):
    max_value = 0
    seeds = []

    file = open(filename, 'r')
    count = 0

    while True:
        # Get next line from file
        line = file.readline()
        if not line:
            break
        if count == 0:
            max_value = line
        else:
            seeds = line.split(',')
        count += 1

    file.close()

    return max_value, seeds

def read_test_data(filename):
    vectors = []

    file = open(filename, 'r')
    count = 0

    while True:
        # Get next line from file
        line = file.readline()
        if not line:
            break
        line = line.replace('\n', '')
        vectors.append(line.split(','))

        count += 1

    file.close()

    return vectors

def load_bloom_filter(filename):
    # Open a file: file
    file = open(filename,mode='r')
    
    # read all lines at once
    all_of_it = file.read()
    
    # close the file
    file.close()

    return all_of_it


def read_model(filename):
    bloom_filters = []
    seeds = []

    file = open(filename, 'r')

    while True:
        # Get next line from file
        line = file.readline()
        if not line:
            break
        
        line = line.replace('\n', '')
        seed = int(line, 10)
        number = ''
        while line and not line == '\n':
            line = file.readline()
            number += line
        number = number.replace('\n', '')

        bloom = bitarray(number)

        seeds.append(seed)
        bloom_filters.append(bloom)
        if not line:
            break

    file.close()

    return bloom_filters, seeds

from bitarray import bitarray
import trainer


def read_model(filename):
    bloom = None
    seeds = []

    file = open(filename, 'r')
    line = file.readline()
    if not line:
        return bloom, seeds

    line = line.replace('\n', '')
    seeds = line.split(' ')
    while True:
        # Get next line from file
        number = ''
        while line:
            line = file.readline()
            number += line
        number = number.replace('\n', '')

        bloom = bitarray(number)

        if not line:
            break

    file.close()

    return bloom, seeds

def read_data(filename):
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

def detect(model_path, data_path, b, r, prime_factor):
    print('started detecting son')
    bloom, seeds = read_model(model_path)

    for i in range(len(seeds)):
        seeds[i] = int(seeds[i], 10)


    data = read_data(data_path)

    if not len(data) > 0:
        return []

    shingles_num = len(data)
    docs_num = len(data[0])

    sig_mat = trainer.compute_singature_matrix(data_path, seeds, docs_num, shingles_num)
    bands_mat = trainer.banding(sig_mat, b, r, docs_num, prime_factor)

    result = [False for _ in range(docs_num)]

    for band in bands_mat:
        for i in range(len(band)):
            hash_value = band[i]
            if hash_value < shingles_num and (bloom[hash_value] == 1 or bloom[hash_value] == '1'):
                result[i] = True
    print('done detecting son')
    print(result)

    



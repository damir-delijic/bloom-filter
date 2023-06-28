
from bitarray import bitarray
import trainer
from tqdm import tqdm


def read_model(filename):
    bloom = None
    seeds = []

    file = open(filename, 'r')

    line = file.readline()
    if not line:
        return bloom, seeds
    line = line.replace('\n', '')
    seeds = line.split(' ')

    line = file.readline()
    if not line:
        return bloom, seeds
    number = line.replace('\n', '')
    bloom = bitarray(number)

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
        vector = line.replace('\n', '').split(',')
        vectors.append(vector)

        count += 1

    file.close()

    return vectors

def detect(model_path, data_path, b, r):
    print('Started detection son')

    bloom, seeds = read_model(model_path)
    # print('Bloom: ', bloom)
    # print('Seeds: ', seeds)


    for i in range(len(seeds)):
        seeds[i] = int(seeds[i], 10)

    bloom_size = len(bloom) # nije zapravo prime faktor
    print('Size of bloom: ', bloom_size)

    print('Readin test data')
    data = read_data(data_path)

    if not len(data) > 0:
        return []

    shingles_num = len(data)
    docs_num = len(data[0])
    print('Number of shingles: ', shingles_num)
    print('Number of documents: ', docs_num)

    print('Computing signature matrix')
    sig_mat = trainer.compute_singature_matrix(data_path, seeds, docs_num, shingles_num)

    print('Banding stage')
    bands_mat = trainer.banding(sig_mat, b, r, docs_num, bloom_size)

    result = [0 for _ in range(docs_num)]

    for band in bands_mat:
        for i in range(len(band)):
            hash_value = band[i]
            if bloom[hash_value] == 1 or bloom[hash_value] == '1':
                result[i] = 1
    
    print('Finished detecting son')
    return result
    



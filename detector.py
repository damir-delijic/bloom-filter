
from bitarray import bitarray
import trainer


def read_model(filename):
    blooms = []
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
        blooms.append(bloom)
        if not line:
            break

    file.close()

    return blooms, seeds


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

def detect(model_path, data_path):


    blooms, seeds = read_model(model_path)

    k = len(seeds)

    data = read_data(data_path)

    if not len(data) > 0:
        return []

    shingles_num = len(data)
    corpus_size = len(data[0])

    result = [1 for _ in range(corpus_size)]

    for i in range(k):
        bloom = blooms[i]
        vector = trainer.initialize_signature_vector(corpus_size=corpus_size, fake_infinity=shingles_num)
        seed = seeds[i]
        max_r = shingles_num

        for j in range(len(data)):
            row = data[j]
            trainer.update_vector_signatures(vector=vector, seed=seed, row=row, row_num=j, modulator=max_r)

        for j in range(len(vector)):
            doc_minhash = vector[j]
            if result[j] == 1:
                if doc_minhash < max_r and (bloom[doc_minhash] == 1 or bloom[doc_minhash] == '1'):
                    pass
                else:
                    result[j] = -1

    print(result)



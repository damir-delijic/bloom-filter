import helper
from bitarray import bitarray

max_value, seeds = helper.read_detection_parameters('filter\\parameters.txt')

max_value = int(max_value, 10)

for i in range(len(seeds)):
    seeds[i] = int(seeds[i], 10)

data = helper.read_test_data('data\\test.txt')

bloom = helper.load_bloom_filter('filter\\bloom_filter.txt')
bloom = bitarray(bloom)


signatures = helper.initialize_signature_matrix(len(data[0]), len(seeds), max_value)



count = 0

for row in data:
    helper.update_signatures(signatures, seeds, row, count, max_value)
    count += 1

result = [0 for _ in range(len(data[0]))]

for i in range(len(signatures[0])):
    for j in range(len(signatures)):
        if bloom[signatures[j][i]] == '1' or bloom[signatures[j][i]] == 1:
            result[i] += 1
        else:
            pass

print(result, len(signatures))



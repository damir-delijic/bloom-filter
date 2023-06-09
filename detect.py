import helper

filters, seeds = helper.read_model('model\\bloom_filter.txt')

print(filters, seeds)

data = helper.read_test_data('data\\test.txt')

number_of_shingles = len(data)
number_of_documents = len(data[0])

print('doc nums', number_of_documents)
print('shingle nums', number_of_shingles)

result = [True for _ in range(number_of_documents)]

for i in range(len(seeds)):
    signature_vector = helper.initialize_signature_vector(number_of_documents, number_of_shingles)
    seed = seeds[i]

    for row_num in range(len(data)):
        vector = data[row_num]
        helper.update_vector_signatures(signature_vector, seed, vector, row_num, number_of_shingles)

    bloom_filter = filters[i]

    for j in range(len(signature_vector)):
        j_doc_hash = signature_vector[j]
        if bloom_filter[j_doc_hash] == 1 or bloom_filter[j_doc_hash] == '1':
            result[j] = result[j] and True
        else:
            result[j] = result[j] and False

print(result)



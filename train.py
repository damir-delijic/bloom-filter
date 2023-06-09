import helper

# valjalo bi da broj singlova bude prost ili da ima sto vise njegovih osobina
# bira se m na osnovu n, pa na osnovu toga se racuna optimalno k

filename = 'data\\train.txt' # rucno se unosi

number_of_documents = 0
number_of_shingles = 0

file = open(filename, 'r')

while True:
    # Get next line from file
    row = file.readline()
    if not row:
        break
    if number_of_shingles == 0:
        number_of_documents = len(row.replace('\n', '').split(','))
    number_of_shingles += 1

number_of_bits_in_bloom_filter = number_of_shingles
number_of_hash_functions = helper.calculate_number_of_hash_functions(number_of_documents, number_of_bits_in_bloom_filter)
number_of_hash_functions = 2
# generise seedove za hes funkciju, jedna hes fja + k seedova = k hes fja
# seeds = helper.generate_seeds(number_of_hash_functions)
seeds = [3, 4]

print('singles num', number_of_shingles)
print('docs num', number_of_documents)
print('seeds num', number_of_hash_functions)
print('seeds', seeds)

for i in range(number_of_hash_functions):
    #  inicijalizacija blumovog filtera
    bloom_filter = helper.initialize_bloom_filter(number_of_bits_in_bloom_filter)
    print('filter', bloom_filter)
    # inicijalizacija matrice signatura
    signature_vector = helper.initialize_signature_vector(number_of_documents, number_of_shingles)

    # cita iz fajla liniju po liniju i racuna potpise
    file = open(filename, 'r')
    row_num = 0

    while True:
        # Get next line from file
        row = file.readline()
        if not row:
            break

        vector = row.replace('\n', '').split(',')
        
        helper.update_vector_signatures(signature_vector, seeds[i], vector, row_num, number_of_shingles)
        row_num += 1

    file.close()

    for j in range(len(signature_vector)):
            position = signature_vector[j]
            bloom_filter[position] = 1

    isFirst = i == 0
    helper.save_bloom_filter(bloom_filter, seeds[i], "model\\bloom_filter.txt", isFirst)






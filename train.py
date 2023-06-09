import helper

# valjalo bi da broj singlova bude prost ili da ima sto vise njegovih osobina
# bira se m na osnovu n, pa na osnovu toga se racuna optimalno k

max_value = 499 # broj singolva rucno se unosi
filename = 'train.txt' # rucno se unosi

n = 50 # broj dokumenata u korpusu
m = 2**10 # broj bita u filteru
k = helper.calculate_number_of_hash_functions(n, m)

# generise seedove za hes funkciju, jedna hes fja + k seedova = k hes fja
seeds = helper.generate_seeds(k)

#  inicijalizacija blumovog filtera
bloom = helper.initialize_bloom_filter(m)

# inicijalizacija matrice signatura
signatures = helper.initialize_signature_matrix(n, k, max_value)

# cita iz fajla liniju po liniju i racuna potpise
file = open(filename, 'r')
count = 0

while True:
    # Get next line from file
    row = file.readline()
    if not row:
        break
    helper.update_signatures(signatures, seeds, row, count, max_value)
    count += 1

file.close()

for i in range(len(signatures)):
    for j in range(len(signatures[i])):
        position = signatures[i][j]
        bloom[position] = 1

helper.save_bloom_filter(bloom, "filter\\bloom_filter.txt")

helper.save_parameters_necessary_for_detection(max_value, seeds, "filter\\parameters.txt")




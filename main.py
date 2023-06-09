import helper

# valjalo bi da broj singlova bude prost ili da ima sto vise njegovih osobina
# bira se m na osnovu n, pa na osnovu toga se racuna optimalno k

max_value = 499 # broj singolva rucno se unosi
filename = 'dataset.txt' # rucno se unosi

n = 50 # broj dokumenata u korpusu
# m = 2**30 # broj bita u filteru
# k = helper.calculate_number_of_hash_functions(n, m)
k = 5
# m = 2**12

# generise seedove za hes funkciju, jedna hes fja + k seedova = k hes fja
# seeds = helper.generate_seeds(k)
seeds = [5, 15, 26, 57, 65]
print('Seeds: ', seeds)

#  inicijalizacija blumovog filtera
# bloom = helper.initialize_bloom_filter(m)

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
    
for i in range(len(signatures)):
    printstr = 'h(' + str(i)  + ') = '
    
    for j in range(len(signatures[i])):
        printstr += (str(signatures[i][j]) + ' ')

    print(printstr)

file.close()

# print(signatures)
# for i in range(len(signatures)):
#     printstr = 'h(' + str(i)  + ') = '
    
#     for j in range(len(signatures[i])):
#         printstr += (str(signatures[i][j]) + ' ')

#     print(printstr)



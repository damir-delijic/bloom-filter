import random

number_of_documents = 2
number_of_shingles = 7
sparcity_percentage = 90
sparcity_deviation = 3
filename = "data\\test.txt"

print('started')
    
with open(filename, "w") as myfile:
    for i in range(0, number_of_shingles):
        for j in range(0, number_of_documents):
            random_num = random.randint(1, 100)

            if (j < number_of_documents * 0.3 and i < number_of_shingles * 0.5) or (j > number_of_documents * 0.7 and i > number_of_shingles * 0.5):
                if random_num < sparcity_percentage - sparcity_deviation:
                    myfile.write('1')
                else:
                    myfile.write('0')
            else:
                myfile.write('0')

            if(j == number_of_documents - 1):
                if(i == number_of_shingles - 1):
                    pass
                else:
                    myfile.write('\n')
            else:
                myfile.write(',')

print('all done son')
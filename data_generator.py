import random

number_of_documents = 10
number_of_shingles = 10
sparcity_percentage = 72
filename = "data\\train.txt"

print('started')
    
with open(filename, "w") as myfile:
    for i in range(0, number_of_shingles):
        for j in range(0, number_of_documents):
            random_num = random.randint(1, 100)
            if(random_num < 91):
                myfile.write('0')
            else:
                myfile.write('1')

            if(j == number_of_documents - 1):
                if(i == number_of_shingles - 1):
                    pass
                else:
                    myfile.write('\n')
            else:
                myfile.write(',')

print('all done son')
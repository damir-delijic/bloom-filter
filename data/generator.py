import random
from tqdm import tqdm

def generate_two_clusters(filename, number_of_documents, number_of_shingles):
    with open(filename, "w") as myfile:
        for i in tqdm(range(0, number_of_shingles)):
            for j in range(0, number_of_documents):
                random_num = random.randint(1, 100)

                if (j < number_of_documents * 0.1 and i <= number_of_shingles * 0.5) \
                or (j > number_of_documents * 0.9 and i > number_of_shingles * 0.5):
                    if random_num < 58:
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

def generate_two_test_clusters(filename, number_of_documents, number_of_shingles):
    with open(filename, "w") as myfile:
        for i in tqdm(range(0, number_of_shingles)):
            for j in range(0, number_of_documents):
                random_num = random.randint(1, 100)

                if (j <= number_of_documents * 0.5 and i <= number_of_shingles * 0.5) or (j >= number_of_documents * 0.5 and i > number_of_shingles * 0.5):
                    if random_num < 58:
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

def generate_uniform(filename, number_of_documents, number_of_shingles):
      with open(filename, "w") as myfile:
        for i in tqdm(range(0, number_of_shingles)):
            for j in range(0, number_of_documents):
                random_num = random.randint(1, 100)
                if random_num < 15:
                    myfile.write('1')
                else:
                    myfile.write('0')

                if(j == number_of_documents - 1):
                    if(i == number_of_shingles - 1):
                        pass
                    else:
                        myfile.write('\n')
                else:
                    myfile.write(',')

def generate_test(filename, number_of_documents, number_of_shingles):
     with open(filename, "w") as myfile:
        for i in tqdm(range(0, number_of_shingles)):
            for j in range(0, number_of_documents):
                random_num = random.randint(1, 100)

                if number_of_shingles * 0.45 <= i and i <= number_of_shingles * 0.55:
                    if random_num < 58:
                        myfile.write('1')
                    else:
                        myfile.write('0')
                else:
                    myfile.write('0')
                    
                # if random_num > 81:
                #     myfile.write('1')
                # else:
                #     myfile.write('0')

                if(j == number_of_documents - 1):
                    if(i == number_of_shingles - 1):
                        pass
                    else:
                        myfile.write('\n')
                else:
                    myfile.write(',')

# number_of_train_documents = 3000
# number_of_test_documents = 20
# number_of_shingles = 12007

number_of_train_documents = 500
number_of_test_documents = 50
# number_of_shingles = random.randint(2000, 4000)
number_of_shingles = 3989 # prime

# print('started')
# print('generating training data')
# generate_two_clusters('train.txt', number_of_train_documents, number_of_shingles)
# print('generating test data')
# # generate_two_clusters('test.txt', number_of_test_documents, number_of_shingles)
# # print('all done son')

# print('generating test data')
# generate_two_test_clusters('test.txt', number_of_test_documents, number_of_shingles)
# print('all done son')
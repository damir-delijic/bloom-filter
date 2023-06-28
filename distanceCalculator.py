import trainer
from tqdm import tqdm

def calculate(training_file_path, testing_file_path, similarity_limit):

    print('Started computing similarities son')

    number_of_train_documents, shingles_num = trainer.calculate_characteristic_matrix_dimensions(training_file_path)
    number_of_test_documents, shingles_num = trainer.calculate_characteristic_matrix_dimensions(testing_file_path)


    # redovi test dokumenti
    # kolone train dokumenti
    # prva koordinata presjek
    # druga unija
    similarity_matrix = [ [ [0, 0] for _ in range(number_of_train_documents) ] for _ in range(number_of_test_documents) ]

    training_file = open(training_file_path, 'r')
    testing_file = open(testing_file_path, 'r')

    print('Reading file line by line')
    pbar = tqdm(total=shingles_num)
    count = 0
    while True:
        # Get next line from file
        train_line = training_file.readline()
        test_line = testing_file.readline()
        if not train_line or not test_line:
            pbar.close()
            break

        #imaju isti broj linija ali im linije nisu iste duzine
        
        train_vec = train_line.replace('\n', '').split(',')
        test_vec = test_line.replace('\n', '').split(',')
        for i in range(len(test_vec)):
            test_document = test_vec[i] # ovo je u stvari 0 ili 1 odnosno da li sadrzi taj singl
            for j in range(len(train_vec)):
                train_document = train_vec[j] # ovo je 0 ili 1, da li testni dokument sadrzi singl
                if str(test_document) == "1" and str(train_document) == "1": # ako oba sadrze ovaj singl onda se povecava presjek
                    similarity_matrix[i][j][0] += 1
                elif str(test_document) == "0" and str(train_document) == "1":
                    similarity_matrix[i][j][1] += 1 # ako barem jedan onda uniju povecava
                elif str(test_document) == "1" and str(train_document) == "0":
                    similarity_matrix[i][j][1] += 1 # ako barem jedan onda uniju povecava
                else:
                    pass

        pbar.update(1)

    training_file.close()
    testing_file.close()

    print('Calculating similarities')
    for i in tqdm(range(len(similarity_matrix))):
        result = 0
        for j in range(len(similarity_matrix[i])):
            temp = similarity_matrix[i][j]
            sim = temp[0] / (temp[0] + temp[1])
            if sim > similarity_limit:
                result += 1
            
        similarity_matrix[i] = result

    print('Finished calculating similarites son')
    return similarity_matrix
    



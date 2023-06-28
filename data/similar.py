file = open('train.txt', 'r')
temp = open('verySimilar.txt', 'w')

number_of_differences = 2
number_of_shingles = 3989

num = 50
count = 0
while True:
    # Get next line from file
    line = file.readline()

    if not line:
        break
    vector = line.replace('\n', '').split(',')

    for i in range(num):
        if count == 100 or count == 400:
            if vector[i] == "0":
                temp.write("1")
            else:
                temp.write("0")
        else:
            temp.write(vector[i])
        if i == num - 1:
            temp.write('\n')
        else:
            temp.write(',')

    count += 1

temp.close()
file.close()
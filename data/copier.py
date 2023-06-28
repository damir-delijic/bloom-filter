file = open('train.txt', 'r')
temp = open('test.txt', 'w')

num = 50
while True:
    # Get next line from file
    line = file.readline()

    if not line:
        break
    vector = line.replace('\n', '').split(',')

    for i in range(num):
        temp.write(vector[i])
        if i == num - 1:
            temp.write('\n')
        else:
            temp.write(',')

    
    
temp.close()
file.close()
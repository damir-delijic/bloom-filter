import trainer
import detector
import distanceCalculator
# prime_around_gigabyte = 8589934609

# prime_around_megabyte = 8388617

train_file = 'data\\train.txt'
permutations_num = 100
bands_num = 20
rows_num = 5

# trainer.train(train_file, permutations_num, bands_num, rows_num)

test_file = 'data\\identical.txt'
model_file = 'model\\bloom.txt'


detectionResult = detector.detect(model_file, test_file, bands_num, rows_num)

calculationResult = distanceCalculator.calculate(train_file, test_file, 0.9)

print('Detection | Calculation')
for i in range(len(detectionResult)):
    print(detectionResult[i], calculationResult[i])

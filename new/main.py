import trainer
import detector

prime_around_gigabyte = 8589934609

prime_around_megabyte = 8388617

train_file = 'data\\train.txt'
permutations_num = 25
bands_num = 5
rows_num = 5

trainer.train(train_file, permutations_num, bands_num, rows_num, prime_around_megabyte)

test_file = 'data\\test.txt'
model_file = 'model\\bloom.txt'


detector.detect(model_file, test_file, bands_num, rows_num, prime_around_gigabyte)

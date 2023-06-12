import trainer
import detector
import temp


trainer.train('data\\train.txt', 'model\\bloom.txt')
detector.detect('model\\bloom.txt', 'data\\test.txt')
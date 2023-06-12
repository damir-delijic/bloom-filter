import trainer
import detector


trainer.train('data\\train.txt', 'model\\bloom.txt')
detector.detect('model\\bloom.txt', 'data\\test.txt')
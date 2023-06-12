import trainer
import detector

print("bloom method: ")
trainer.train('data\\train.txt', 'model\\bloom.txt')
detector.detect('model\\bloom.txt', 'data\\test.txt')

import numpy as np
from sklearn import svm


train_data_list = detector.read_data('data\\train.txt')
train_data_np_arr = np.array([np.array(xi) for xi in train_data_list])
X_train = np.transpose(train_data_np_arr)


test_data_list = detector.read_data('data\\test.txt')
test_data_np_arr = np.array([np.array(xi) for xi in test_data_list])
X_test = np.transpose(test_data_np_arr)

# # fit the model
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(X_train)
y_pred_test = clf.predict(X_test)

print("one class sv method: ")
print(y_pred_test)


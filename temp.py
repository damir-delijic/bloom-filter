

import numpy as np
from sklearn import svm

import helper

train_data = helper.read_test_data('data\\train.txt')

x_tr = np.array([np.array(xi) for xi in train_data])

X_train = np.transpose(x_tr)

test_data = helper.read_test_data('data\\test.txt')

x_tes = np.array([np.array(xi) for xi in test_data])

X_test = np.transpose(x_tes)

# fit the model
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(X_train)
y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)

print(y_pred_test)


train.train()
detect.detect()
#
# MLpractice.py
#
# work on trying out different ML techniques with the cancer data set
#
# LKS, July 2016, Insight
#
import numpy as np
import glob
import matplotlib.pyplot as plt
from sklearn.svm import LinearSVC
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier 
data=np.genfromtxt(glob.glob('cancerData.txt')[0], delimiter=',')
#
# column 11 is what tells us if cancer is present or not
#
data=data[~np.isnan(data).any(axis=1)]

dataSwap=np.swapaxes(data, 1, 0)
#

    
#
#
X=np.swapaxes(np.array(dataSwap[1:-1]),1,0)
Y=np.array(dataSwap[-1]).ravel()
Y.reshape((len(Y),1))
#
#
X_train, X_test, y_train, y_test = cross_validation.train_test_split(
    X, Y, test_size=0.5, random_state=1)
print X_train.shape, y_train.shape
print X_test.shape, y_test.shape

clf = LinearSVC(C=1).fit(X_train, y_train)
print("Accuracy for LinearSVC: %0.4f" % clf.score(X_test, y_test))

clf= RandomForestClassifier(n_estimators=10)
clf.fit(X_train,y_train)
print("Accuracy for RandomForest Classifier: %0.4f" % clf.score(X_test, y_test))

from sklearn import svm
clf = svm.SVR()
clf.fit(X_train, y_train)
print("Accuracy for SVM: %0.4f" % clf.score(X_test, y_test))
#
# okay but we need ranked paramters? 

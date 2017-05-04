from sklearn import svm
X = [[0, 0], [2, 2]]
y = [0.5, 2.5]
clf = svm.SVR()
a = clf.fit(X, y)
print(a)
b = clf.predict([[1, 1]])
print(b)
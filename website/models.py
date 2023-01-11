#from sklearn import datasets, svm, metrics

#iris = datasets.load_iris()

#n_samples = len(iris.data)
#data = iris.data

#classifier = svm.SVC(gamma=0.001)

#classifier.fit(data[:n_samples // 2], iris.target[:n_samples // 2])

#expected = iris.target[n_samples // 2:]
#predicted = classifier.predict(data[n_samples // 2:])

#def predict(arr):
#	return classifier.predict([arr])
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

iris = load_iris()

data = iris.data
target = iris.target

model = KNeighborsClassifier()
model.fit(data, target)
def predict(arr):
	return model.predict([arr])

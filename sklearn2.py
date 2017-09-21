import  numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets

n_neighbors = 15

iris = datasets.load_iris()
X = iris.data[:,:2]
y = iris.target

h = 0.02

cmap_light = ListedColormap(['#FFAAAA','#AAFFAA','#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000','#00FF00','#0000FF'])

clf = neighbors.KNeighborsClassifier(n_neighbors,weights='uniform')
clf.fit(X,y)

x_min, x_max = X[:, 0].min() -1 , X[:, 0].max() +1
y_min, y_max = X[:, 1].min() -1 , X[:, 1].max() +1

xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

#print(xx[:2,:5],yy[:2,:5])
print(xx)
print(yy)
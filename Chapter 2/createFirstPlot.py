from numpy import *
import kNN
import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
datingDataMat,datingLabels = kNN.file2matrix('datingTestSet2.txt')
# ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
ax.scatter(datingDataMat[:,1], datingDataMat[:,2],
           15.0*array(datingLabels), 15.0*array(datingLabels))
plt.show()
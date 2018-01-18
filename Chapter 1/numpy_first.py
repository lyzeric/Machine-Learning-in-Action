from numpy import *
array = random.rand(4,4)
print(array)

print()

randMat = mat(random.rand(4,4))
print(randMat.I) #矩阵求逆

print()

invRandMat = randMat.I
print(randMat * invRandMat)

print()

myEye = randMat * invRandMat
print(myEye - eye(4)) #eye单位矩阵


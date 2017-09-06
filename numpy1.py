import numpy as np

a = np.array([[1,2,3],[4,5,6]],float)
print(a)

b=a.flatten()
print(b)

c=list(b)
print(c)

x=np.arange(9,36,3)
y=np.split(x,3)
print(x)
print(list(y[0]))


k=list(a[:,:])
print(k[1])


T = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
for i in T :
    for j in i:
        print(j)

print(a(axis=0))
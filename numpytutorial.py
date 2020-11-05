#numpy tutorial
import numpy as np 
import math
a = np.array([1, 2, 3])
print(a)
print(a.ndim)

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(b.shape)

print(a.dtype)

c = np.array([2.2, 5., 1.1])
print(c.dtype.name)

d = np.zeros((2,3))
print(d)

e = np.ones((2,3))
print(e)

ee = np.random.rand(2,3)
print(ee)

f = np.arange(10, 50, 2)
print(f)

ff = np.linspace(0,2, 15)
print(ff)

a = np.array([10,20,30,40])
b = np.array([1,2,3,4])

c = a-b
print(c)

d = a*b
print(d)

#farenheit conversion
farenheit = np.array ([0, -10, -5, -15, 0])

celcius = (farenheit - 31) * (5/9)
print(celcius)
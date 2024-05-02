'''multidimensional array library
speed is 50x more faster compare to python list
numpy uses fixed types
5 -> 8 bit -> numpy-> int32 or you can customize to int16 or int 8

ex 5 in binary : 00000101

Why NumPy ?
Because it is faster.
why it is faster ?

because it uses fixed type:
ex 5 in binary : is 00000101
In numpy u can represent type as int32(4 bytes), Int 16 or int 8

while in python list: it has to store other information as well
like size,object type, refrence count, onject value=> each 8 byte, single
integer in list takes a lot more space.

numpy uses less memory, while iterating we don't have to type check
numpy uses contiguous memory like in C.

list in python can be scatterd(stored refrences of values in memory),
 but numpy makes sure to use continous memory blocks

CPU SIMD(sigle instruction multiple data) vector processing units,
effective cache utilization, keep closer where you need them

Difference:

List: We can do CRUD ops in List and it is same for NumPy
but a lot more things with NumPy

Application of NumPy: MATLAB replacement and SciPy as well
Plotting: MatPlotLib
As Backend for : Pandas, Digital Photography
Most Important for ML/AI

'''
import numpy as np
#initilization

a = np.array([1,2,3])
print(type(a))

b=np.array([[1,3,4],[0.4,0.5,0.8]])

print(b)

#get dims

print(b.ndim)
print(b.shape)

print(a.dtype) #int32 #b.dtype float64


from numpy import *
arr=array([

    [1,2,3,4,5],
    [6,7,8,9,10]
])
print(arr.ndim)
print(arr.shape)
print(arr.dtype)

arr1=array([

    [1,2,3,4,5],
    [6,7,8,9,10]
])
arr2=arr1.flatten()
arr2=arr.reshaped(2,3,4)
print(arr2)

m=('1 2 3 4 5 ; 6 7 8 9 10' )
print(m)
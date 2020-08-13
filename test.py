import numpy as np
from function import typeof
from function import *
from COOGRID1 import COOGRID

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr)
# print(arr.shape)
# print(arr.shape[0])
# print(arr.shape[1])
# print(arr.shape[2])

def shift(arr,k,l=None):
    if size(arr)[0] == 1 :
        if arr.any() == None:
            raise ValueError('输入空数组，无法移位')
        lens=len(arr)
        k %= lens
        while k != 0 :
            tmp = arr[lens-1]
            i = lens - 1
            while i > 0:
                arr[i] = arr[i-1]
                i -= 1
            arr[0] = tmp
            k -= 1
        return arr
    if size(arr)[0] == 2 :
        if arr.any() == None:
            raise ValueError('输入空数组，无法移位')
        s1 = int(size(arr)[1])
        k %= s1
        s2 = int(size(arr)[2])
        l %= s2
        while k != 0 :
            i = s1 - 1
            tmp = arr[i:]
            while i > 0:
                arr[i,:]=arr[i-1,:]
                i -= 1
            arr[0,:] = tmp
            k -= 1
        while l != 0 :
            tmp = arr[:,s2-1]
            i = s2 - 1
            while i > 0:
                arr[:,i] = arr[:,i-1]
                i -= 1
            arr[:,0] = tmp
            l -= 1
        return arr

# brr=np.array([1,2,3])
# print(shift(brr,1) )
#print(arr[0,:])
print(shift(arr,1,1))
#print(arr[2,:])
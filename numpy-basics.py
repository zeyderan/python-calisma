import numpy as np

#python list
py_list = [1,2,3,4,5,6,7,8,9]

#numpy array
np_array = np.array(py_list) # parametre olarak liste alır

# print(type(py_list))
# print(type(np_array))

np_multi = np_array.reshape(3,3) # reshape dizi yapısını yeniden şekillendirme

print(np_multi)

print(np_multi.ndim)
print(np_multi.shape)
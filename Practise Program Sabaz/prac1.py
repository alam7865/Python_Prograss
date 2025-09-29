# import numpy as np
# arr=np.array(2)
# print(arr)
# print(arr.dtype)
# print(arr.shape)


# /////////////////////// 1 D array ////////////////////////
# import numpy as np
# arr=np.array([2,3,4,5,6,7,8])
# print(arr)
# print(arr.shape)
# print(arr.dtype)

# /////////////////////////////////////////////

# import numpy as np
# arr=np.array([2,3,4,5,6],ndmin=5)
# print(arr)
# print(arr.dtype)
# print(arr.ndim)
# print(arr.shape)


# ////////////////////////////// Array Reshaping ///////////////////////////////
# import numpy as np
# arr=np.array([1,2,3,4,5,6])
# newarray=arr.reshape(3,2,-1)
# print(newarray)


# /////////////////////////////

# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarray=arr.reshape(2,3,2)
# print(newarray)
# print(newarray.ndim)

# newarray=arr.reshape(3,3)
# print(newarray)


# /////////////////////////////////// Copy (creates new ones) and view (stores the reference) //////////////////////////

# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# x=arr.copy()
# y=arr.view()

# print(x.base) # copy --> None
# print(y.base) # view --> Original array

# # x[0]=100

# # print(arr)
# # print(x)


# y[0]=55
# print(y)
# print(arr)


# ////////////////////////////////// Reshape ///////////////////////////

# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# # newarr=arr.reshape(2,6)
# newarr=arr.reshape(2,3,-1)
# print(newarr)


# ////////////////////////////////// convert array into 1 D array ////////////////////////////////

# import numpy as np
# arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# newarray=arr.reshape(10)
# print(newarray)


# /////////////////////////////////// Numpy Iteration ///////////////////////////
# import numpy as np

# ////// for 1 D

# arr=np.array([1,2,3,4,5,6])

# for x in arr:
#     print(x)

# ////////////////  for 2 D

# arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])

# for x in arr:
#     for y in x:
#         print(y,end=" ")
#     print("\nHello")    


# ////////////////// for 3 D

# arr=np.array([[[1,2,3,4,5]],[[6,7,8,9,10]]])
# for x in arr:
#     for y in x:
#         print(y,end=" ")
#     print("Hello")    


# ///////////////////////////////// nditer ///////////////////////

# arr=np.array([[[[1,2,3,4,5],[6,7,8,9,10]]]])

# for x in np.nditer(arr):
#     print(x)


# ///////////////////////////////// skip 1 element in nditer //////////

# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])

# arr=np.array([[1,2,3,4],[5,6,7,8]])
# for x in np.nditer(arr[:, ::2]):
#  print(x)


# /////////////
# /////////////
# ///////////////////////////////// Enumerate for 1 D array ////////////

# arr=np.array([1,2,3,4,5])
# for x,item in np.ndenumerate(arr):
#     print(x,item)


# /////////////////////////////// Enumerate for 2 D array /////////////

# arr=np.array([[[1,2,3,4,5],[6,7,8,9,10]]])
# for idx,item in np.ndenumerate(arr):
#     print(idx,item)




# /////////////////////////////////// Join //////////////////////////////

# arr1=np.array([1,2,3,4])
# arr2=np.array([10,11,12,13])
# arr3=np.concatenate((arr1,arr2))
# print(arr3)

# ////////////////////////////////// split /////////////////////////////

# import numpy as np
# arr=np.array([1,2,3,4,5,6])
# arr1=np.array_split(arr,4)
# print(arr1)

# ////////////////////////////////// split access /////////////////////

# import numpy as np
# arr=np.array([1,2,3,4,5,6])
# arr1=np.array_split(arr,4)
# print(arr1[0])
# print(arr1[1])
# print(arr1[2])

# //////////////////////////////// split the 2 D array into 2 D array /////////////
# import numpy as np
# # arr=np.array([1,2,3],[4,5,6],[7,8,9])
# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

# newarr = np.array_split(arr, 5)
# # newarr=np.array_split(arr,3)
# print(newarr)


# ///////////////////////////////// Search 2 D matrix ///////////////////////////
# import numpy as np
# arr=np.array([2,3,4,5,4,2,2,3,3])
# newarry=np.where(arr==2)
# print(newarry)

# ///////////////////////////////// Search even element indices /////////////////////////

# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8])
# evenIdx=np.where(arr%2==0)
# oddIdx=np.where(arr%2!=0)
# print(evenIdx)
# print(oddIdx)


# //////////////////////////////// sort the array /////////////////////////////////////
import numpy as np
arr=np.array([6,5,7,1,4,2,3])

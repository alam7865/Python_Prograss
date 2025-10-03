# import numpy as np
# print(np.__version__)

# //// numpy array 

# import numpy as np
# arr=np.array([1,2,3,4,5,6])
# print(arr)


# /////////////// Array Dimension

# 1) 0 Dim array

# import numpy as np
# arr=np.array(42)
# print(arr)
# print(arr.shape)            # 0
# print(arr.ndim)             # 0

# 2) 1 Dim array

# import numpy as np
# arr=np.array([1,2,3,4])
# print(arr)
# print(arr.ndim)       # 1
# print(arr.shape)

# 3) 2 Dim array

# import numpy as np
# arr=np.array([[1,2,3,4],[5,6,7,8]])
# print(arr)
# print(arr.shape)    # (2, 4)

# 4) 3 Dim array


# import numpy as np
# arr=np.array([[[1,2,3,4],[5,6,7,8]]])
# print(arr)
# print(arr.shape)    # (2, 4)
# print(arr.ndim)     # 3


# ///////////////////// we can specify the dimension by ourself
# import numpy as np
# data=np.array([1,2],ndmin=5)
# print(data.shape)       # (1, 1, 1, 1, 2)


# ///////////////////// Accessing Values ///////////////////////////////

# import numpy as np
# arr=np.array([1,2,3])

# print(arr[0])   # 1


# import numpy as np
# arr=np.array([[1,2,3],[4,5,6]])
# print(arr[0,1])     # 2


# /////////////// Numpy Slicing /////////////////////////
# import numpy as np
# arr=np.array([1,2,3,4,5])

# # ///// slice 0-5
# n=len(arr)

# print(arr[0:n])         # [1 2 3 4 5]

# print(arr[:n])            #[1 2 3 4 5]

# print(arr[2:])              # [3,4,5]

# print(arr[:])               #[1 2 3 4 5]

# print(arr[:-1])               # [1 2 3 4]

# print(arr[-1])                  # 5


# ///////////// Skip some of steps i.e 2

# print(arr[0:n:2])       # [1 3 5]



# ///////////////////////////////////////////////////////////////
# arr1=[1,2,3,4]
# print(type(arr1))       # list




# import numpy as np
# dd=np.array([1,2,3])
# print(dd.dtype)      # int64


# import numpy as np
# arr=np.array([1,2,3,4],dtype=str)
# print(arr)              # ['1' '2' '3' '4']
# print(arr.dtype)        # <U1



# import numpy as np
# arr=np.array(['1','2','3','4'],dtype=int)
# print(arr)      # [1 2 3 4]

# ====> It will throw an error
# import numpy as np
# arr=np.array(['1','2','Three',4],dtype=int)
# print(arr)   # ValueError: invalid literal for int() with base 10: 'Three'


# ////////////////////////// Converting data type on existing data /////////////////

# import numpy as np
# arr1=np.array([1.2,2.2,3.2,4.5,6.7])

# arr2=arr1.astype(int)
# print(arr2)  # [1 2 3 4 6]
# print(arr1)  # [1.2 2.2 3.2 4.5 6.7]

# arr2=arr1.astype(str)
# print(arr2)
# print(arr2.dtype)   #int 32


# ////////////////////////// copy and view

# copy:It creates a new array
# view:It is just the view of the original array

# import numpy as np
# arr1=np.array([1,2,3,4,5])
# arr1[0]=10
# arr2=arr1.copy()
# arr2[4]=1000
# print(arr1)
# print(arr2)




# ////////////////////
# ///////views

# import numpy as np
# arr1=np.array([1,2,3,4,5])
# arr2=arr1.view()
# arr1[0]=5
# # arr2[0]=55
# print(arr1)  # [5 2 3 4 5]
# print(arr2)  # [5 2 3 4 5]


# ///////////////////////////
# //////// Base

# import numpy as np
# arr1=np.array([5,10,15,20])
# arr2=arr1.copy()
# arr3=arr1.view()
# print(arr2.base)    # None because arr2 is a copy
# print(arr3.base)    # [ 5 10 15 20] beacause it is view and it gives the original array


# //////////// Numpy array reshaping 

# import numpy as np
# arr1=np.array([1,2,3,4,5,6,7,8,9,10])

# arr2=arr1.reshape(2,1,5)
# print(arr2)



# ///////////////// Looping throw numpy

# import numpy as np
# arr1=np.array([1,2,3,4,5,6,7,8,9])

# for x in arr1:
#     print(x,end=" ")


import numpy as np
arr1=np.array([[1,2,3],[4,5,6]])

# for x in arr1:
#     print(x)


for x in arr1:
    for y in x:
        print(y,end=" ")









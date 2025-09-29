# import numpy as np
# arr=np.array(2)
# print(arr)
# print(arr.dtype)
# print(arr.shape)


# ////////////////////////////////////////////////////

# import numpy as np
# # arr=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
# arr=np.array([1,2,3,4,5])
# print(type(arr))
# # print(arr.shape) # (5,)

# //////////////////////////////////////////////////////

# import numpy as np
# arr=np.array([1,2,3,4,5],ndmin=5)
# print(type(arr))
# print(arr.shape)


# //////////////////////////////////////////// array reshape /////////////////////////

# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8])
# # newarr=arr.reshape(3,4)
# print(arr.shape(2,2,-1))
# # print(newarr.shape)


# ///////////////////////////////////// iterating in 2d array /////////////////////////

# import numpy as np
# arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])

# for x in arr:
#     for y in x:
#         print(y,end=" ")



# ///////////////////////////////////// iterate on 3D array /////////////////////////
# import numpy as np
# arr=np.array([[[1,2,3,4,5],[6,7,8,9,10]]])

# for x in arr:
#     for y in x:
#         for z in y:
#             print(z,end=" ")


# for x in np.nditer(arr):
#     print(x)



# low = 1
# high = 999
# target = 899


# while low<=high:
#     mid=low+(high-low)/2

#     if mid==target:
#         print("Found 😊")
#         break
#     elif mid>target:
#         high=mid-1
#     else:
#         low=mid+1


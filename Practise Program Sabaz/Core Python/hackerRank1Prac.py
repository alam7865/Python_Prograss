
# //////////////// Hacker Rank Problems on pandas ////////////
# ////////// Arrays

# import numpy
# def arrays(arr):
#     # complete this function
#     # use numpy.array
    
#     arr1=numpy.array(arr,float)
#     n=len(arr)//2
#     n1=len(arr)-1
#     x=0
#     while x<n:
#         a=arr[x]
#         b=arr[n1]
        
#         arr1[x]=b
#         arr1[n1]=a
#         x+=1
#         n1-=1
#     return arr1


# 2)////////////// Shapes and reshape 

# import numpy as np


# arr=np.array(list(map(int,input().split())))

# arr1=arr.reshape(3,3)
# print(arr1)


# 3)///////////// Zeros and Ones

# import numpy as np
# shape = tuple(map(int,input().split()))
# print(np.zeros(shape,dtype = int))
# print(np.ones(shape,dtype = int))


# 4)///////////// Sum and Prod

# import numpy as np
# shape = tuple(map(int,input().split()))
# print(np.zeros(shape,dtype = int))
# print(np.ones(shape,dtype = int))


# 5)///////////// Floor, Ceil and Rint

# import numpy as np

# arr=list(map(float,input().split()))
# arr2=np.array(arr)
# np.set_printoptions(legacy='1.13')

# print(np.floor(arr2)) 
# print(np.ceil(arr2)) 
# print(np.rint(arr2)) 



# 6)////////////// Max and Min 

# import numpy as np

# arr1=list(map(int,input().split()))
# x=arr1[0]
# y=arr1[1]

# arr = np.array([list(map(int, input().split())) for _ in range(x)])

# min1=np.min(arr,axis=1)

# minimum=-1

# for x in min1:
#     if minimum<x:
#         minimum=x

# print(minimum) 



# 7)//////////////// Dot and Cross

# import numpy as np

# N = int(input())

# A = np.array([list(map(int, input().split())) for _ in range(N)])
# B = np.array([list(map(int, input().split())) for _ in range(N)])

# print(np.matmul(A, B))


# 8)/////////////// Inner and Outer

import numpy as np
A=np.array(list(map(int,input().split())))
B=np.array(list(map(int,input().split())))

print(np.inner(A,B))
print(np.outer(A,B))

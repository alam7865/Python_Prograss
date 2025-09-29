# ////////////////////////////////// Week 4 //////////////////////////////////////
# ////////////////
#  ////////////////////// Enumerate ///////////////////

# ==>It adds a counter/Index towards any iterable items
# list=[1,2,3,4,5,6]   # list
# list=(1,2,3,4,5)       # Tuple

# for x in list:
#     print(x,end=" ")


# ////  Enumerator ///

# for x,val in enumerate(list,start=2):
#     print(x,val)



# /////////////// Zip /////////////////////
# ==>It used to combine any iterable element by element in tuple

# list1=[2,4,6,8,10]
# list2=[1,3,5]

# list3=tuple(zip(list1,list2))
# print(list3)              # ((2, 1), (4, 3), (6, 5))


# for i,j in zip(list1,list2):
#     print(i,j)  2 1   4 3   6 5






# ////////////// break ///////////////////
# ==>It used to terminate the programm

# for x in range(1,10+1,1):
#     if x==5:
#         break
#     print(x,end=" ")   # 1 2 3 4


# //////////// continue /////////////////
# ==>It uses to Skip the current iterations

# i=1
# while True:
#  if i==5:
#     continue
#  if i==10:
#     break
#  print(i,end=" ")
#  i+=1


# i=0
# while True:
#     i+=1
#     if i==5:
#         continue
#     if i==10:
#         break
#     print(i,end=" ")




# ///////////////////////////// efficient iterator ////////////////////////
# 1)Loop instead of while Loop

# for x in range(10):
#     print(x,end=" ")


# 2)Enumerator 

# list=[1,3,5,7,9]
# for idx,val in enumerate(list):
#     print(idx,val)

# 3)Zip

# idx=[1,2,3,4,5]
# elem=["apple","mango","orange","banana","grapes"]

# for idx,elem in zip(idx,elem):
#     if idx==4:
#         print(idx,elem,end=" ")

# 4)list comprension

# list2=[x*x for x in range(1,10)]
# print(list2)

#Use Biult in Function
# list=[1,2,3,4,5]
# x=sum(list) # 15
# x=max(list)  
# x=min(list)  # 1
# x=any(list)
# x=all(list)
# print(x)


# ////////// list comprenension ////////////
# ==>It is consise way to create a list using single line of code

# list=list((1,2,3,4,5,6))
# print(list)


# /////////// Lambda function ///////////////
# ==>It is a anonomous function that takes any number of argument but it has only one expression

# list=[1,2,3,4,5]
# from functools import reduce
# x=int(reduce((lambda x,y:x+y),list))
# print(x)


# ////////////// comments ///////////////////
# ==> comments are written by the python developer to Explain the Python code 
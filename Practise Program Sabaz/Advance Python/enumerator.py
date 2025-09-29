# //////////////////////////// enumerator ///////////////////////////
# enumerator: It adds counter/index towards any iterable items

# arr=[1,2,3,4,5,6,7,8,9,10]

# for index,elem in enumerate(arr):
#     print(index,elem)

# ///////////////////////////////  start index from 1

# for index,elem in enumerate(arr,start=1):
#     print(index,elem)



# /////////////////////////////// Iterator //////////////////////////

# Iterator:It uses to iterate throw any list or tuple etc
arr=[1,2,3,4,5,6]

# 1)Iterate element directly

# for x in arr:
#     print(x,end=" ")

#2)Iterate element throw index

# for x in range(len(arr)):
#     # print(x,end=" ")
#     print(arr[x],end=" ")



# ///////////////////////////// Decorator ///////////////////////////
# ==> it is a function that uses to add a  extra feature to the function without changing the code 

# def div(a,b):
#     print(a//b)

# def smartdev(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return inner     
    

# div=smartdev(div)
# div(2,4)    # 2
# div(4,2)    # 2


# ////////////////////////// @decorator syntax /////////////////////////////

# def smartDiv(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return inner

# @smartDiv
# def div(a,b):
#     print(a//b)

# div(2,4)    


# /////////////////////////// deep and shallow copy ////////////////////
# import copy
# arr=[1,2,3,4,5]
# shallow=copy.copy(arr)
# deep=copy.deepcopy(arr)

# arr[0]=100
# print(shallow)
# print(deep)

# /////////////////////////////////////////////////////////////
# import copy
# arr=[[1,2,3],[4,5,6]]
# shallow=copy.copy(arr)
# deep=copy.deepcopy(arr)

# arr[0][0]=100
# print(shallow)
# print(deep) 

# //////////////////////// Recursion : Sum of digit ///////////////////



# def digitSum(n,k,ispp):
#     s1=str(n)
#     if len(s1)<=1:
#         return s1
#     sum=0
#     for x in s1:
#         sum+=int(x)
#         print(sum, "sum")

     
#     if ispp==1:
#         sum*=k
#         ispp=0
#     ss=str(sum)    
#     return digitSum(sum,k,ispp)   

# x=digitSum("148",2,1)      
# print(x)   
 


#  ////////////////////////////////// generator function //////////////////////////////////////////
# ==>Any function can become generator by writing the yielf

# def top10():
#     i=1
#     while i<=10:
#         yield i
#         i+=1
# values=top10()

# for x in values:
#     print(x)


# /////////////////////////// Difference between enumerator or iterator ///////////////

                        # Iterator                           Enumerator
# What it returns  |	Only the element/value.  	       | A pair (index, value).
# Use case	       |   When you only need the values.	   | When you need both index & value at the same time.



# ///////////////////////////////// Generator /////////////////////////////////////////

# 1)example1: print natural Number

# def printNum(n):
#     for x in range(1,n+1):
#         yield x

# num=printNum(5)

# for x in num:
#     print(x,end=" ")


# 2)example2: print Even Number

# def printEven(n):
#     for x in range(2,n+1,2):
#         yield x

# num=printEven(10)

# for x in num:
#     print(x,end=" ")



# 3)example3: print fibonacchi series 

def printFib(x,y,z):
    print(x,y,end=" ")

    for i in range(2,z,1):
        sum=x+y
        # print(sum,end=" ")
        yield sum
        x=y
        y=sum

num=printFib(0,1,5)

for x in num:
    print(x,end=" ")


# 4)example 4:print square of number

# def square(n):
#     for x in range(1,n+1,1):
#         # print(x*x,end=" ")
#         yield x*x

# num=square(5)
# for x in num:
#     print(x,end=" ")



# //////////////////////////////// regular expression ///////////////////////////////

# import re
# text="Hello I have 2 mango and 3 banana my mobile mango number is 1234567890"

# /////// Find all the match pattern

# result=re.findall(r"\d+",text)
# print(result)       # it gives us list ['2', '3', '1234567890']


# ///////////// search all the patterns in string ////////////

# result1=re.search("mango",text)     
# print(result1)            # # <re.Match object; span=(15, 20), match='mango'>

# result1=re.search("mango",text)  
# print(result1.group())   # mango ---> It Returns the first match

# ///////////////// match pattern ///////////////////////////
# text2=re.match("mango",text)
# print(text2.group())



# https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true
# https://www.hackerrank.com/challenges/matching-word-non-word/problem?isFullScreen=true




# //////
# //////////
# 1. Character Classes

# import re

# text = "My age is 25, id=A123"

# # [0-9] or \d → digits
# print(re.findall(r"\d", text))  
# # ['2', '5', '1', '2', '3']

# # \w → letters, numbers, underscore
# print(re.findall(r"\w", "Hi_99"))  
# # ['H', 'i', '_', '9', '9']


# 2. Anchors
# # ^ → must start with
# print(bool(re.match(r"Hello", "Hello World")))  
# # True

# # $ → must end with
# print(bool(re.search(r"World$", "Hello World")))  
# # True




# ////////////////// Common Symbol
#  . → any single character
# print(re.findall(r"h.t", "hat hot hit hut"))  
# # ['hat', 'hot', 'hit', 'hut']

#  * → 0 or more
# print(re.findall(r"ab*", "a ab abb abbb"))  
#  ['a', 'ab', 'abb', 'abbb']

#  + → 1 or more
# print(re.findall(r"ab+", "a ab abb abbb"))  
#  ['ab', 'abb', 'abbb']

#  ? → 0 or 1
# print(re.findall(r"ab?", "a ab abb abbb"))  
#  ['a', 'ab', 'ab', 'ab']

#  {} → exact count
# print(re.findall(r"\d{3}", "My pin is 12345"))  
#  ['123']
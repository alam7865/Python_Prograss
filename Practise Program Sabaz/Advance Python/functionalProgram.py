# //////////////////////////  Pure function  ////////////////////////

# def add(a,b):
#     return a+b

# x=add(5,5)
# print(x)

# /////////////////////// Impure function /////////////////////////

# x=5
# def func(a):
#     global x
#     x=x+a
#     return x


# res=func(x)
# print(res)
# print(x)



# ////////////////////// Iterator and enumerator ////////////////
# nums=[1,2,3,4,5]
# it=iter(nums)
# # print(it.__next__())
# # print(it.__next__())
# # print(it.__next__())
# # print(it.__next__())
# # print(it.__next__())
# # print(it.__next__())
# # print(it.__next__())

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# //// Iterator in python
# nums=[1,2,3,4,5,6]

# # for x in nums:
# #     print(x)

# it=iter(nums)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))



# //////////// Enumerator //////////////////////////
# list1=["apple","mango","orange","banana","grapes"]
# for index,item in enumerate(list1):
#     print(index,item)


# ////////////////// Decorators ////////////////////

# def div(a,b):
#     return a//b


# def smartdiv(func):
#     def inner(a,b):
#         if a<b:
#          a,b=b,a
#         return func(a,b)
#     return inner

# div=smartdiv(div)
# print(div(4,2))     

# ////////////////// @ smartdiv ///////////////////



# def smartdiv(func):
#     def inner(a,b):
#         if a<b:
#          a,b=b,a
#         return func(a,b)
#     return inner

# @smartdiv
# def div(a,b):
#     return a//b

# # div=smartdiv(div)
# print(div(2,4))  



# ///////////////////// split and join /////////////////////
# ssss=str(input("Enter string"))
# print(ssss)
# ss="Hello Sabaz Alam"
# str=ss.split(" ")
# ss1="-".join(str)
# print(ss1)


# ///////////////////find occurance ///////////////////
# str1="ABCDCDC"
# str2="CDC"

# len1=len(str2)
# count=0
# for x in range((len(str1))-(len1)+1):
#     str=str1[x:x+len1]
#     print(str)
#     if str==str2:
#         count+=1
#     # print(x)

# print(count)

# //////////////////////////////////////
# def average(array):
#     # your code goes here
#     set1=set()
#     sum=0
#     count=0
#     for x in array:
#         if set1.add(x):
#             count+=1
#             sum+=x
    
#     print("SUM: ",count)
#     # ans=sum/count
#     # return ans
#     return 5



# def avg(array):
#     sum=0
    
#     set1=set(array)
#     for x in set1:
#         sum+=x
    
#     ans=sum/len(set1)
#     print(ans)


# x=avg([161,182,161,154,176,170,167,171,170,174])
# print(x)



# ////////////////////////////////////// regular expression /////////////////////////////
# import re
# text="Hello my name is Gopal and i am 12 year or 20 year old my number is 1234567891"
# res=re.findall(r"\d+",text)
# re.findall(r"\d+", text)
# print(res)

# /////////////// search  the first number only/////////////////
# res=re.search(r"\d+",text)
# print(res.group())

# ////////////////// Match a text //////////////////////////////
# ss=re.match(r"Hello",text)
# print(ss.group())




# ////////////////////////// text operation i.e Regular expression ////////////
text="Hello my name is Gopal and i am 12 year or 20 year old my number is 1234567891"

import re
#////////////////// find all numbers in text //////////////////////

# txt1=re.findall(r"\d+",text)
# print(txt1)

# //////////////////////////   search  ///////////////////////////
# tt1=re.search(r"\d+",text)
# print(tt1.group())

# ///////////////////////// Search all text //////////////////////
result2 = re.match(r"Hello", text)
print(result2)






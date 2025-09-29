# 1)print leap 
# 2)print function
# 3)set

# Functional Programming	Introduction, Pure and Impure functions
# Lambda Functions	Usage with map(), filter(), reduce()


# //////////////////////// Functional Programming //////////////////////////

# /////////// Pure Function ////////////////////////

# def add(a,b):
#     return a+b

# ans=add(5,5) 
# print(ans)


#//////////// Impure Function /////////////////////// 

# def add1(a,b):
#  print(a+b)

# add1(5,10)

# ////////////// map : Manuplate every element//////////

# arr=[1,2,3,4,5]

# output=list(map((lambda x:x+1),arr))
# print(output)

# //////////////////// filter: filter out the list based on condtion //////////////

# arr=[1,2,3,4,5,6,7,8,9,10]
# output=list(filter((lambda x: x>5),arr))
# print(output)


# /////////////////// Reduce: It uses to take all the element of array and come out with a single solution out of them

# from functools import reduce
# arr=[1,2,3,4,5,6,7,8,9,10]
# output=int (reduce((lambda x,y:x+y),arr))
# print(output)


# /////////////////// Recursion: function calling itself is called recursion ///////////////////////

# 1)sum of 5 number

# def sum(num):
#     if num<=0:
#         return 0
#     return num+sum(num-1)

# res=sum(5)
# print(res)

# 2)Product of 5 number

# def pro(num):
#     if num==1:
#         return 1
#     return num*pro(num-1)

# ans=pro(5)
# print(ans)


# ///////////////////////////////////// Hacker Rank Problem ///////////////////////////////////////
# ss="hello kk"
# print(ss.title())



# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true			



# ////////////////// regular expression /////////////////////////////////
import re
text="Hello I have 2 mango and 3 banana my mobile mango number is 6002744852"

# /////// Find all the match pattern

# result=re.findall(r"\d+",text)
# print(result)       # it gives us list ['2', '3', '6002744852']


# ///////////// search all the patterns in string ////////////

# result1=re.search("mango",text)     # <re.Match object; span=(15, 20), match='mango'>
# print(result1.group())

# ///////////////// match pattern ///////////////////////////
text2=re.match("mango",text)
print(text2.group())
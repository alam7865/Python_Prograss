# Iterator:It iterate through any list,tuple,etc

# nums=[1,2,3,4,5]
# it=iter(nums)
# print(next(it))
# print(next(it))
# print(next(it))



# ////////////////// pure function /////////////////////

# def add(a,b):
#     return a+b

# x=add(5,5)
# print(x)

# ///////////////// Impure function ///////////////////

# def add(a,b):
#     print(a+b)

# add(5,6)


# ///////////////// Lambda function //////////////////

# x=lambda x:x+5
# res=x(5)
# print(res)


# ////////////// map filter reduce ////////////////////

# num=[1,2,3,4,5]

# num1=list(map(lambda x:x+1,num))
# print(num1)


# //////////////////// filter ///////////////////////
# num=[1,2,3,4,5]
# num1=list(filter(lambda x:x>=3,num))
# print(num1)

# //////////////////// reduce ///////////////////////

# num=[1,2,3,4,5]
# from functools import reduce
# ans=int(reduce(lambda x,y:x+y,num))
# print(ans)

# /////////////////// recursion //////////////////////

# def rec1(num):
#     if num<=0:
#         return 0
#     return num+rec1(num-1)

# ans=rec1(5)
# print(ans)



# /// product

# def pro(num):
#     if num<=1:
#         return 1
#     return num*pro(num-1)

# ans=pro(5)
# print(ans)


# ///////////////// Iterator ///////////////////////

# num=[1,2,3,4,5]
# it=iter(num)

# print(next(it))
# print(next(it))
# print(next(it))

# /////////////////// enumerator /////////////////
# num=[1,2,3,4,5]

# for idx,val in enumerate(num,start=1):
#     print(idx,val)


# dict1={'a':[1,2,3],'b':[5,10,15]}

# # for x in dict1:
# #     print(x,dict1[x])

# for idx,val in enumerate(dict1):
#     print(idx,val,dict1[val])



# /////////////////// Decorators /////////////////////
# Decorators:It a function that adds extra feature to the code without changing the code

# def div(a,b):
#     print(a//b)

# def smartDev(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return inner

# div=smartDev(div)
# div(2,4)      


# ////////////////////////// generators /////////////////////////

# num=[1,2,3,4,5,6,7,8,9,10]
# def even(num):
#     for x in num:
#         if x%2==0:
#             yield x

# res=even(num)

# # for x in res:
#     # print(x)
# print(res)

# /////// fibnocchi

# def printFib(num):
#     print(0,1,end=" ")
#     a=0
#     b=1
#     n=num-2
#     while n!=0:
#         sum=a+b
#         print(sum,end=" ")
#         a=b
#         b=sum
#         n-=1
        

# printFib(5)

# res=printFib(5)

# for x in res:
#     print(x,end=" ")



# //// Custom Decorators


# def smartDev(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return inner

# @smartDev
# def div(a,b):
#     print(a//b)

# div(4,2)    



# /////////////// zip: It combines element by element in tuple


# list1=[1,3,5,7,9,11]
# list2=[2,4,6]

# list3=list(zip(list1,list2))
# print(list3)


# ////////////////// list comprehension //////////////////////////////
# list1=list(("apple","mango","orange","banana","grapes"))
# print(list1)


# list1=("apple","mango","orange","banana","grapes")
# print(type(list1))
# print(list1)

# ///////////////////// lambda and f string ///////////////////

# data=12
# print(f"The value of Data is : {data:.2f}")


# //////////////////////// File Handling ////////////////////

# ////////// read ///////////

# with open("./text.txt","r") as f:
#     print(f.read())

# //////// Write ////////////
# with open("./text3.txt","a") as f:
#     print(f.write("\n 1 2 3 4 5 6 7 8 9 saabb"))

# ///create a file //////////

# with open("./text4.txt","x") as f:
#     print(f.write("HEllo Wheeli oo"))



# ///////////////////// Regular Expression ////////////////////
# import re
# txt="Hello my name is sabaz alam pin:12345 number 12345678910 and 2,3,4"
# res=re.findall(r"\d+",txt)
# print(res)


# 2)/////////// search
# import re
# txt="Hello my name is sabaz alam pin:12345 number 2345678910 and 2,3,4  1111111111"
# res=re.search(r"\d{10}",txt)
# print(res.group())

# 3)////////// Match

# import re
# txt="Hello my name is sabaz alam pin:12345 number 2345678910 and 2,3,4  1111111111"
# res=re.match("my",txt)
# print(res.group())

# ////////////////////////// try catch ///////////////

# try:
#     num1=int(input())
#     num2=int(input())
#     print("Sum: ",num1+num2)
# except:
#     print("Some Thing went wrong")
# finally:
#     print("Programm Ended")       
# 
# 
# //////////////////////////////////////////////////////////////////////////////////////////////


# for input    apple 20
# N=2
# while N!=0:
#     num=input().split()
#     print(num[0])
#     print(int(num[1])*10) 
    #   N=N-1


# N=1
# while N!=0:
#     num=list(map(str,input().split()))
#     # a=num[0]
#     # b=num[1]
#     # c=num[2]
#     # print(a)
#     # print(b)
#     # print(c)
#     a=num[:-1]
#     b=int(num[-1])
#     a1=" ".join(a)
#     print(a1)
#     print(b)
#     N=N-1



# ///////////////////// search substring in string //////////////

# str="abckkabc"
# str2="abc"

# len1=len(str)+1
# len2=len(str2)
# count=0
# for x in range(len1-len2):
#     ss=str[x:x+len2]
#     if ss==str2:
#         print(ss)
#         count+=1
# print(count)        


# ////////////////////// capatalized /////////////////////////////
str="hello Alam"

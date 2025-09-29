# import module1
# x=module1.greet("Kalam")
# print(x)


# /////////////////////// args and kwargs /////////////////
# def func(*para):
#     print(para)
#     print(para[0])

# func(1,2,3,4)   # All extra element will be in tuple

# def func1(**para):
#     # print(para["lastname"],para["state"])
#     print(para)

# func1(lastname="Alam",firstname="Sabaz",state="Hydrabad")


# /////////////////////////// perform and operation //////////////////////
# print(2&3)






# ///////////////////////////// Lambda function ///////////////////////////
# x=lambda x:x+1
# print(x(5))

# /// Map////


# nums=[1,2,3,4,5]

# output=list(map(lambda x:x+1,nums))
# print("Sum",output)


# //////////// Filter ////////////////////////////
# nums=[1,2,3,4,5]
# output=list(filter(lambda x:x>3,nums))
# print(output)


# //////////////// Reduce /////////////////////////

# from functools import reduce

# nums=[1,2,3,4,5]
# output=int(reduce(lambda x,y:x+y,nums))
# print(output)


# /////// Recursion /////////////

#/////////// Addition of N number

# def rec(num):
#     if num<=0:
#         return 0
#     return num+rec(num-1)

# res=rec(5)
# print(res)

# ////////// Sum of N number

# def pro(num):
#     if num<=0:
#         return 1
#     return num*pro(num-1)

# ans=pro(5)
# print(ans)


# ////////////////////////////////// Iterator and enumerator ///////////////////////
# /////// Enumerator

# def enumerator1(nums):
#     for index,val in enumerate(nums):
#         print(index,val)

# enumerator1([1,2,3,4,5])


# nums=[1,2,3,4,5]

# for index,val in enumerate(nums):
#     print(index,val)

# ////////////////////////////////// iterator //////////////////////////////////

# nums=[1,2,3,4,5]

# for x in range(len(nums)):
#     print(x,nums[x])



# ///////////////////////////////// Decorators //////////////////////////////

# def div(a,b):
#     print(a//b)

# def smartdiv(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)   
#     return inner

# div=smartdiv(div)
# div(4,2)


# /////////////////////////////////////////////////////////////////////////
def my_gen():
    yield 1
    yield 2
    yield 3

for val in my_gen():
    print(val)


# //////////////////////////////// Int Float boolean String /////////////////////////
# x=5
# y=2.34
# # z="10"
# z="10"
# zz=True

# print(type(x))
# print(type(y))
# print(type(z))
# print(type(zz))


# x1=float(x)
# print(x1)

# y1=int(y)
# print(y1)



# z1=int(z)
# print(z1)

# /////////////////////////////////////// Arathematic ////////////////////////////

# Arathematic operation --> + - * /

# 1) Addition
# a=5
# b=5

# print("Sum: ",a+b)

# 2)Subtraction
# print(a-b)

# 3)Multiplication
# print(a*b)

# 4)Division

# print(a//b)


# ////////////////////////////////////////// Logical Operator //////////////////////////
# 1)And
# 2)Or
# 3)Not


# a=False
# b=False

# # and :should Satisfy All the condition
# print(a and b)

# # or :Should satisfy any one of the Condtion
# print(a or b)

# # 3)Not Operator : Reverse of or and Not Operator


# //////////////////////////// Assignment Operator /////////////////////////

# y=5
# y1=5
# print(y+y1)

# /////////////////////////// String Manuplation //////////////////////////

# str="Hello World"
# # 1)Concatenation
# str1=str+" "+"Sabaz Alam"
# print(str1)


# 2) Slicing

# str="Hello Sabaz Alam"
# print(str[0:5])
# print(str[1:])
# print(str[:])

# 3)Python common Build in method
# str="Hello Sabaz Alam"
# str1=str.upper()    # HELLO SABAZ ALAM
# str1=str.replace('H','K')    # HELLO SABAZ ALAM
# str1=str.split()
# print(str1)

# //// join
# str1='.'.join(['a','b','c'])
# print(str1)

# /////////////////////// split and join extra character ///////////////////
str="apple"
# str1=str.split()
# print(str1)
# res=""

# for x in range(len(str)-1):
#     res+=str[x]+"#"

# res+=str[len(str)-1]
# print(res)

ss="#".join(str)
print(ss)
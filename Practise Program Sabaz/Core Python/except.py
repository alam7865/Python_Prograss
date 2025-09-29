# n=int(input())
# n=1

# while n!=0:
#    num=list(map(int,input().split()))
#    a=num[0]
#    b=num[1]
#    if b==0:
#         print("Error Code: integer division or modulo by zero")
#    elif b>=0 & b<=9:
#           print(a%b)  
#    else:
#         print(f"Error Code: invalid literal for int() with base 10: {b}")
#    n=n-1



#/////////////////////////////////////////////////////////////////////////////////////
# n=int(input())
# n=1

# while n!=0:
#    num=list(map(int,input().split()))
#    a=num[0]
#    b=num[1]
#    if b==0:
#         print("Error Code: integer division or modulo by zero")
#    elif b>=0 & b<=9:
#           print(a%b)  
#    else:
#         print(f"Error Code: invalid literal for int() with base 10: {b}")
#    n=n-1



n=int(input())
n=1

while n!=0:
   try:
    num=list(map(int,input().split()))
    a=num[0]
    b=num[1]
    try:
      print(a%b)
    except ZeroDivisionError: 
      print("Error Code: integer division or modulo by zero")
   except ValueError as e:
        print(f"Error Code: {e}")
   n=n-1     
      

#    if b==0:
#         print("Error Code: integer division or modulo by zero")
#    elif b>=0 & b<=9:
#           print(a%b)  
#    else:
#         print(f"Error Code: invalid literal for int() with base 10: {b}")
#    n=n-1


print(1%3)
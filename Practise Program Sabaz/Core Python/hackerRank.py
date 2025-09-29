#/////////////////// collection counter

# list=[]

# for x in range(5):
#     list.append(int(input()))

# print(list)
# txt=list(input("Enter the text"))

# print(txt)
# dict1={}

# for x in txt:
#     if x in dict1:
#         dict1[x]=dict1.get(x)+1
#     else:
#         dict1[x]=1    

# print(dict1)


# //////////////// input ////////////////////////
# list=[2,3,4,5,6,8,7,6,5,18]


# n=int(input())
# list=[]

# for x in range(n):
#     list.append(int(input()))

# print(list)
# dict1={}

# for x in list:
#     if x in dict1:
#         dict1[x]=dict1.get(x)+1
#     else:
#         dict1[x]=1  


# print(dict1)    
# 
# num=int(input())
# sum=0
# while num!=0:
#     x=int(input())
#     y=int(input())

#     if(dict1.get(x)>0):
#         sum+=y
#         dict1[x]=dict1.get(x)
#         if dict1.get(x)<=0:
#             del dict1[x]
#     num-=1

# print(sum)            



# n = int(input())

# shoe_sizes = list(map(int, input().split()))

# inventory = {}

# for x in shoe_sizes:
#     if inventory.get(x, 0) > 0: 
#         inventory[x] = inventory.get(x, 0) + 1
#     else:
#         inventory[x] = 1 


# m = int(input())

# earnings = 0

# for _ in range(m):
#     size, price = map(int, input().split())
#     if inventory.get(size) > 0:        
#         earnings += price
#         inventory[size]=inventory.get(size)-1     

# print(earnings)




# ////////////////////// char list in dict
list=['a','a','b','a','b']
dict={}

# how to put list in dict like this {'a':[1,2,4], 'b':[3,5]}

for idx,val in enumerate(list,start=1):
    if val not in dict:
        dict[val]=[]
    dict[val].append(idx)

print(dict)   

list2=['a','b']

for x in list2:
    if x not in dict:
        print(-1)
    else:
        print(dict.get(x))    



# ///////////////////////////////////////////

# n, m = map(int, input().split())

# list1 = input().split()   
'a', 'a', 'b', 'a', 'b'
dict1 = {'a':[1,2,4],
         'b':[3,5]}


# for idx, val in enumerate(list1, start=1):
#     if val not in dict1:
#         dict1[val] = []
#     dict1[val].append(idx)


# list2 = input().split()  
list2=['a','b']

for x in list2:
    if x not in dict1:
        print(-1)
    else:
        print(" ".join(map(str, dict1.get(x))))

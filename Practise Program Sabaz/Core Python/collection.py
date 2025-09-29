# s, n = map(str, input().split())
# n=int(n)

# dict1={}



n1=int(input())

while n1!=0:
 num = list(map(str, input().split()))
 a1=num[0]
 a2=int(num[1])

 dict1={}
 
 if a1 not in dict1:
    print(a1,a2)
    dict1[a1]=a2   
 n1=n1-1    
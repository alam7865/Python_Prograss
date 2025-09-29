# txt="Hello my name is Sabaz Alam and my number is 1234567890 and 2234567891"
# import re
# # res=re.search("my12",txt)
# # print(res)   # None

# ans=re.findall(r"\d+",txt)
# print(ans)


# ////////////////// zip ///////////
list1=[1,2,3,4,5,6,7]
list2=[2,4,6]
# list3=list(zip(list1,list2))
# print(list3)                # <zip object at 0x0000020DFEEF9C00>

# for x in list3:
#     print(x,end=" ")


# /////////////// For zip longest //////////////////

# from itertools import zip_longest
# list3 = list(zip_longest(list1, list2))
# print(list3)        # [(1, 2), (2, 4), (3, 6), (4, None), (5, None), (6, None), (7, None)]


from itertools import zip_longest
list3=list(zip_longest(list1,list2,fillvalue=1))
print(list3)
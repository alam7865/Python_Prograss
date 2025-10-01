# Json.dumps: It convert Python Object into json String

# data1={
#     "a":"apple",
#     "b":"mango",
#     "c":"Orange"
# }
# import json
# d1=json.dumps(data1)
# print(type(d1))
# print(d1)

# 2)dump:write json data into file

# import json
# data1={
#     "a1":"apple",
#     "b1":"Ball",
#     "c1":"Cat1"
# }

# with open("./jsonP.json","w") as f:
#     json.dump(data1,f)


# 3)Reading json from a files

# import json
# with open("./jsonP.json","r") as f:
#     dd=json.load(f)
#     print(type(dd))
#     print(dd)


# 4)Converting json String to python object:

# import json

# dd='{"a":"apple","b":"Mango","c":"Cat"}'
# data1=json.loads(dd)
# print(type(data1))  #dict
# print(data1)        # {'a': 'apple', 'b': 'Mango', 'c': 'Cat'}



# /////////////////  order dictionary 

# from collections import OrderedDict
# dict1=OrderedDict()

# # dict1["a"]=1
# # dict1["b"]=2
# # dict1["z"]=3
# # dict1["d"]=4
# # dict1["c"]=5

# dict1[1]="apple"
# dict1[0]="Mango"
# dict1[5]="Banana"
# dict1[3]="Grapes"

# print(dict1)


# //////////////// Default Dictionary ////////////////////

# from collections import defaultdict
# dict1=defaultdict(list)

# dict1["a"]
# dict1["d"]=3
# dict1["b"]=2
# # print(dict1.get("a"))  # 0
# print(dict1["a"])        # 0
# print(dict1["b"])        # 2



# ///////////////// Json Operations //////////////////
# import json

# data = {"name": "Charlie", "age": 30, "city": "Berlin"}
# print(data)         # {'name': 'Charlie', 'age': 30, 'city': 'Berlin'}

# 1)Delete particular key

# del[data["city"]]
# print(data)

# 2)/////////// Check id a particular key is present or not

# if "city" in data:
#     print("City Key is Present")
# else:
#     print("City Key is Not Present")

# # 3)/////////// How do You update key in     

# data["age"]=30

# print(data)



# 3) How to handle json error

# import json
# json_data='{"a":"apple","b":"ball","c":"cat","d":"Dog",}'

# try:
#     data=json.loads(json_data)
#     print(data)
# except json.JSONDecodeError as e:
#     print("Some Thing Went Wrong",e)    # Some Thing Went Wrong




# ///////////////////////// some operation on dataFrame //////////////

# ===>Rename columns

# import pandas as pd
# d2=pd.read_csv("./data1.csv")
# d1=pd.DataFrame(d2)
# d1=d1.rename(columns={"Name":"Names123"})
# print(d1)




# # ///////////////// Reading xls file   /////////////////   =======> Not working

# # import pandas as pd

# import pandas as pd

# # Load the .xlsx file
# df = pd.read_excel('./datas_prac.xlsx', engine='openpyxl')

# # Display the first few rows of the dataframe
# print(df)



# ////////////////////////////////////// data ///////////////////////////////////////

# data='''{
#   "user_id": "U1001",
#   "name": "Alice",
#   "email": "alice@example.com",
#   "phone": "+123456789",
#   "address": {
#     "city": "New York",
#     "state": "NY",
#     "zip": "10001"
#   }
# }'''


# ///////////// print user city /////////
# city1=data["address"]["city"]
# print(city1)    # New York

# phone=data["phone"]
# print(phone)


# /////////////////////////////////

# import json
# data1=json.loads(data)
# print(data1["address"]["city"])   # New York



# //////////////////////////////
# ///////////////// Order Details in Ecomerce

# import json

# data = '''{
#   "order_id": "O12345",
#   "customer": "John Doe",
#   "items": [
#     {"product": "Laptop", "quantity": 1, "price": 1000},
#     {"product": "Mouse", "quantity": 2, "price": 25}
#   ],
#   "status": "Shipped"
# }'''

# data1=json.loads(data)
# # print(data1["items"][0]) # {'product': 'Laptop', 'quantity': 1, 'price': 1000}
# # print(data1["items"][0]["price"])

# sum1=0
# dd1=data1["items"]
# for x in dd1:
#     sum1+=x["price"]
#     # print(x["price"])

# print("Sum: ",sum1)   #1025



# ///////////////// Configuration Setting //////////////

# data='''{
#   "app_name": "ChatApp",
#   "version": "1.0",
#   "features": {
#     "video_call": true,
#     "file_sharing": true,
#     "encryption": "AES256"
#   }
# }'''

# import json
# data1=json.loads(data)

# # Q) Check if file sharing is on or off


# print(data1)
# dd1=data1["features"]["file_sharing"]
# # print(dd1)

# if dd1:
#     print("File Sharing is on")
# else:
#     print("File Sharing is off")    





# import json

# employees_json = '''[
#   {"id": 101, "name": "Sara", "department": "HR"},
#   {"id": 102, "name": "Tom", "department": "IT"},
#   {"id": 103, "name": "Anna", "department": "Finance"}
# ]'''

# # Q) Find employes whose dept is IT

# data1=json.loads(employees_json)

# for x in data1:
#     # print(x["department"])
#     if x["department"]=="IT":
#         print(x)




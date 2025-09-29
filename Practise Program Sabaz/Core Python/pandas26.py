import pandas as pd
list1=[1,2,3,4,5,6]
list3=pd.Series(list1,index=[5,6,7,8,9,10])
# len1=len(list1)
# x1=57
# list3=pd.Series(list1,index=[x for x in range(x1,x1+len1)])
# print(list3)
# print(list3.get(10))   # 6
# print(list3.get(15))   #None
# print(list3[10])        # 6
print(list3[11])        # Error: KeyError


# # ////////////// get a idx value //////////////
# print(list3[57])



# ////////////// Reading csv files and performing operations //////////////////////

# import pandas as pd
# read1=pd.read_csv("./students.csv")
# # print(read1["Name"])
# # print(pd.Series(read1["Name"][3]))   # Sheha
# print(pd.Series(read1["State"][0]))   # Delhi

# ///////////////////////////// store in dict1 as class as key and freq as value /////////

# import pandas as pd
# read1=pd.read_csv("./students.csv")
# dict1={}
# sum=0
# for idx,row in read1.iterrows():
#     cls=row["Class"]
#     mar=row["RollNo"]
#     dict1[cls]=dict1.get(cls,0)+mar
#     sum+=mar

# print(dict1)
# print("Sum: ",sum)


# ///////////////
# import pandas as pd               # **** Yes we can change the series in pandas
# list=[1,2,3,4,5,6]
# read1=pd.Series(list)
# print(read1)
# read1[0]=100
# print(read1)



# //////////////////////////// printing names whose rollno <=5
# import pandas as pd
# read1=pd.read_csv("./students.csv")
# for idx,row in read1.iterrows():
#     nam=row["Name"]
#     roll=row["RollNo"]

#     if roll<=5:
#         print(nam,end=" ")




# ///////////////////////////// Data Frames /////////////////////////////

# import pandas as pd
# data=['Geeks', 'For', 'Geeks', 'is', 
#             'portal', 'for', 'Geeks']

# d1=pd.DataFrame(data)
# print(d1)


# dict1 = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
#         'degree': ["MBA", "BCA", "M.Tech", "MBA"],
#         'score':[90, 40, 80, 98]}

# import pandas as pd

# d1=pd.DataFrame(dict1)   
# # print(d1)   # full data in 2D matrix
# print(d1["score"])



# ////// DataFrames Practise
# import pandas as pd

# data = {
#     "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
#     "Age": [24, 27, 22, 32, 29],
#     "Gender": ["F", "M", "M", "M", "F"],
#     "Salary": [50000, 60000, 45000, 70000, 65000],
# }

# df = pd.DataFrame(data, index=[101,102,103,104,105])  # custom index
# print(df)
# 1. Viewing & Exploring
# print(df.head())        # print all table
# print(df.tail())        # print all tables
# print(df.info())          # give info about table
# print(df.describe())
# print(df.shape)           # descripe the shape (column,row)

# print(df.head(3))
# print(df["Salary"].describe())



# ////////////////////////////////// Selecting Data //////////////////////////
# print(df["Name"])
# print(", ".join(df["Name"]))            # Alice, Bob, Charlie, David, Eve

# print(df["Name"],df["Salary"])

# //// Print name and sal in single

# for name,sal in zip(df["Name"],df["Salary"]):
#     print(name,sal)


#///////////  print by row index

# print(df.loc[101])   # Both are same
# print(df.iloc[0])

# Q) Get the name and Salary of the second Employee

# print(df.iloc[1]["Name"],df.iloc[1]["Salary"])

# /////////////////// Filtering Rows //////////////////////////
# ////print age >=25
# dd=df[df["Age"]>25]
# print(dd)

# Q)Print who Earned more then 60000

# dd=df[df["Salary"]>60000]
# print(dd)

# Q)Print age>25 and Gender="M"
# dd=df[(df["Age"]>25]) & (df[df["Gender"]=="M")]
# dd=df[(df["Age"] > 25) & (df["Gender"] == "M")]
# print(dd)



# 4) Adding / Updating Columns

# //////// Adding and updating Columns
# )/add +5 to all the employs salary

# df["Salary"]=df["Salary"]+5
# print(df["Salary"])

# df["TotalSal"]=df["Salary"]*12

# print(df)


# 6)Sort by Values...

# dd=df.sort_values(by="Salary",ascending=False)
# print(dd)

# 7)Grouping and Aggregation

# dd=df.groupby("Gender")["Salary"].mean()
# print(dd)

# 8) Handling Missing Data

# df.loc[106]=["Sabaz",None,"M",50000]
# # print(df)

# df["Age"].fillna(df["Age"].mean(), inplace=True) 
# print(df)


# 10) Reading and Writing CSV
# rr=pd.read_csv("students.csv")
# df.to_csv("students.csv", index=False)
# print(rr)




# Q)Create a DataFrame of 10 students with Name, Class, Marks, State.

import pandas as pd
d2=pd.read_csv("./data1.csv")
d1=pd.DataFrame(d2)
# print(d1)

# Q)Find the highest Mark student

# print(d1["Marks"].average())
# max1=0

# for marks in d1["Marks"]:
#     max1=max(max1,marks)

# ==>Print the highest mark Student
# print(d1[d1["Marks"]==max1])
# print(marks)


# //////////////// Print Average marks per class
# avg_mark=d1.groupby("Class")["Marks"].mean()
# print(avg_mark)


# //////////////// Sort by marks
# dd=d1.sort_values(by="Marks",ascending=False)
# print(dd)

# //////////////// Remove all Student from particular State
# dd=d1.drop(d1[d1["State"]=="Bihar"].index)
# print(dd)
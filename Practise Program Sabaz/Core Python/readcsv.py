# ////////////////////////////////// File Handling in python //////////////////////
#//////////// read file //////////////////

# 1)Reading file

# f=open("./text.txt","r")
# print(f.read())

# ////////// reading file with data /////////////////
# with open("./text.txt","r") as f:
#     print(f.read())


# 2)Writing file
# with open("./text1.txt","w")as f:
#     f.write("Hello World\n")

# # 3)Append
# with open("./text.txt","a") as f:
#     f.write("Hellllllllo")    



# with open("./text.txt","r") as f:
#     # for line in f:
#     #     print(line.strip())
#     print(f.read())

# 4)Create new file :- If file already present throw error 

# with open("./text2.txt","x") as f:
#     f.write("pppppppppppppppp")



# with open("./text.txt","r+") as f:
#     print(f.read())  # reading file


# with open("./text.txt","r+") as f:
#     f.write("KKKKKKK")  # writing file in text.txt


# //////////////////////// Working with csv/json /////////////////////////////
import pandas as pd
# mydataset={
#         'cars': ["BMV", "Car1", "Tata", "Nano"],
#         'speed': [120, 140, 130, 140]
# }

# print(pd.DataFrame(mydataset)) 

#     
#  cars  speed
# 0   BMV    120
# 1  Car1    140
# 2  Tata    130
# 3  Nano    140


# print(pd.__version__)  # 2.3.2

# a=[1,2,3,4]                 # int64
# a={'a':4,'b':5,'c':7}         #int 64
# a=[2.33,4.23,5.45,3.33]         #float64     0  2.33
# a=('a','b','c','d')         # Object
# print(pd.Series(a))           # Object



# /////////////////////////////// pandas //////////////////////////////////////

# 1)pandas series : A Pandas Series is one-dimensional labeled array capable of holding data of any type (integer, string, float, Python objects etc.). The axis labels are collectively called indexes

# import numpy as np
# import pandas as pd
# data=np.array(['a','e','e','k','s'])
# ser=pd.Series(data)
# print(ser)


# 2)Pandas DataFrame: It is a two-dimensional data structure with labeled axes (rows and columns). It is created by loading the datasets from existing storage which can be a SQL database, a CSV file or an Excel file.

# import pandas as pd 
   
# df = pd.DataFrame()        
                             # Empty DataFrame
                            #  Columns: []
                            #  Index: []
# print(df)

# lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks'] 
  
# df = pd.DataFrame(lst)           
# print(df)

# 0
# 0   Geeks
# 1     For
# 2   Geeks
# 3      is
# 4  portal
# 5     for
# 6   Geeks



# 1)Accessing and modifying the index

# import pandas as pd

# data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
#         'Age': [25, 30, 22, 35, 28],
#         'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
#         'Salary': [50000, 55000, 40000, 70000, 48000]}

# df = pd.DataFrame(data)
# print(df.index)            # RangeIndex(start=0, stop=5, step=1)



# 2)Setting a custom index

import pandas as pd

data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
        'Age': [25, 30, 22, 35, 28],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
        'Salary': [50000, 55000, 40000, 70000, 48000]}

df = pd.DataFrame(data)

df_with_index = df.set_index('Name')   # so name will come as index followed by other
print(df_with_index)
# print(df)


# 3)Resttting the index
# df_reset=df.reset_index()
# print(df)                             # index  name   age   genger  salary  
# print(df_reset)                 # 0      0     John   25    Male   50000


# 4) Indexing with loc

# row=df.loc[0]
# print(row)



# ///////////////////////
# /////////////////////////
# # /////////////////////////////// Pandas accessing DataFrames ////////////////////////

# import pandas as pd

# data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'], 
#         'Age': [25, 30, 22, 35, 28], 
#         'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'], 
#         'Salary': [50000, 55000, 40000, 70000, 48000]}

# df = pd.DataFrame(data)
# Display the entire DataFrame
# print(df)


# 1)Accessing column from DataFrames
# d1=df['Name']
# print(d1)
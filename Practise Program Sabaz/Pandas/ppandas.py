#///////////////////// Read Csv File

# import pandas as pd
# data=pd.read_csv("./Data1.csv",index_col=0)
# # print(data)
# print(data.to_string())

# ///////////////////// Writing FIle to csv //////////////

# import pandas as pd
# data=pd.DataFrame({
# "Name":["sabaz","Kapil","Gopal"],
# "State":["Assam","Bihar","Delhi"],
# "Job":["It","Doctor","Police"]})

# data.to_csv("d1.csv")

# # read the saved data
# rdata=pd.read_csv("./d1.csv",index_col=0)
# print(rdata)



# ////////////////
# //////////////// Read the first row only //////////////
# import pandas as pd
# data1=pd.read_csv("./d1.csv",index_col=0)

# print(data1.iloc[0])  # print first row only

# print(data1.iloc[[0,1]])  # print first and second row only

# print(data1.iloc[0:2])      # print 0 to 1 row only


# /////////////////
# //////////////////// Read only the row where state is Assam

# import pandas as pd
# data=pd.read_csv("./d1.csv",index_col=0)
# print(data[data["State"]=="Assam"])
# print(data[data["Job"]=="Police"])


# //////////////////// Data Exploration /////////////////////
# import pandas as pd
# data=pd.read_csv("./d1.csv",index_col=0)

# print(data.head(2)) # Print first 2 data
# print(data.tail(2))   # Print last 2 data
# print(data.info())    # give infomation about the data
# print(data.describe()) # descripe the data
# print(data.dtypes)       # describe the datatype ---> Object


# ///////////////////// Data Selection and Filtering ////////////////

# import pandas as np
# data=np.DataFrame({
#     "Name":["Sabaz","Mohan","Gopal"],
#     "State":["Assam","Manipur","Delhi"],
#     "Job":["It","Doctor","Fresher"]})


# print(data[data["State"]=="Manipur"])

#/////////////   Print the first Row
# print(data.iloc[[0]])

# ////////////// Print the last Two Row //////////////////////
# print(data.iloc[0:2])

# ////////////// Print only the Name Column //////////////////////
# print(data["Name"])

# ////////////// Select Name and Job Column //////////////////////
# print(data["Name"],data["Job"],end=" ")
# print(data[["Name","Job"]])

# print(data[["Name","Job"]])

# ////////////// Print All rows where job="Doctor" ///////////////////////

# print(data[data["Job"]=="Doctor"])


# ////////////////// Data Manuplation and Data Clearing //////////////////
import pandas as np
data=np.DataFrame({
    "Name":["Sabaz","Mohan","Gopal"],
    "State":["Assam","Manipur","Delhi"],
    "Job":["It","Doctor","Fresher"]})

# print("Original Data: \n",data)
data.loc[2,"Job"]="KK"
print(data)


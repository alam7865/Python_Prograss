# ///////////////    Read to cvs file

# import pandas as pd
# data=pd.read_csv("./Data/d1.csv")
# # print(data)
# print(data.to_string())


# ////////////////   Writing to cvs file ////////////////////////////

# import pandas as pd
# df=pd.DataFrame({
#     "Name":["Alice","Bob","Charlie"],
#     "Age":[12,20,25],
#     "City":["Assam","Delhi","Banglore"]
# })

# df.to_csv("file.csv")

# # Read the data Frame from the file
# data=pd.read_csv("./file.csv",index_col=0)
# print(data.to_string())


# ////////////////////// Write to Cvs File ////////////////////////
# import pandas as pd
# df=pd.DataFrame({"Name":["Sabaz Alam","Rohan","Gopal"],"Age":[12,21,30],"State":["Assam","Bihar","Delhi"]})

# # ///////////////  Writing file i.e CSV in folder
# df.to_csv("Data1.csv")

# ////////////////  Reading that saved File from the Programm

# data=pd.read_csv("./Data1.csv",index_col=0)
# print(data.to_string())


# //////////
# ///////////////////////// Read only the first row

# data=pd.read_csv("./Data1.csv",index_col=0)
# print(data.iloc[[0]])


# ////////////////////////// Print only that row where State="Bihar"

# data=pd.read_csv("./Data1.csv",index_col=0)
# state_row=data[data["State"]=="Bihar"]
# print(state_row)


# ////////////////
# /////////////////////// Reading XLSL File

# import pandas as pd
# data=pd.read_excel("./dfile1.xlsx")
# print(data)

# ///////////////////////////
# import pandas as pd
# filePath=r"C:\Users\FL_LPT-472\Downloads\1mb.xlsx"
# data = pd.read_excel("./filePath","Worksheet")
# print(data)

# ///////////////////////////// Data Exploration /////////////////

# import pandas as pd

# data=pd.read_csv("./Data1.csv",index_col=0)

# dd=data.head()  read from first
# print(dd)

# dd=data.tail()    read from last
# print(dd)

# dd=data.info()
# print(dd)

# dd=data.describe()
# print(dd)

# dd=data.dtypes
# print(dd)




# ////////////////////
# ///////////////////////////////

# Data Selection and Filtering

import pandas as np
data=np.DataFrame({"Name":["Sabaz","Mohan","Gopal"],"State":["Assam","Manipur","Delhi"],"Job":["It","Doctor","Fresher"]})
print(data.iloc[[0]])


"""
read transaction_hdr(1_jan_2019) data and convert it into pandas dataframe, similarly read transaction_dtl_data (1_jan_2019)

"""

import pandas as pd


print("tran_dtl_file: ")
path=r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\tran_dtl_1_2019.csv"
# read tran_dtl_2019 file
df1=pd.read_csv(path)
print(df1)

print("####################################")
print("\n")

print("tran_hdr file : ")
path=r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\tran_hdr_1_2019.csv"
# read tran_hdr_2019 file
df2=pd.read_csv(path)
print(df2)

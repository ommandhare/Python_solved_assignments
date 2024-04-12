"""
read transaction_hdr file with or without header, read without header and assign columns as given in config file

"""


import pandas as pd
import config as cfg

print("####################################")
print("\n")

print("tran_hdr file : ")
path=r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\tran_hdr_1_2019.csv"
# read tran_hdr_2019 file
df=pd.read_csv(path,header=None,names=cfg.e_file_header)


print(df)

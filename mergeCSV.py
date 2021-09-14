from glob import  glob
import pandas as pd
def Merge_CSV(*args):
    print(args)
    print(pd.concat((pd.read_csv).assign(filename=file)for file in args),ignore=True)

Merge_CSV("Orders.csv",",Customers.csv")
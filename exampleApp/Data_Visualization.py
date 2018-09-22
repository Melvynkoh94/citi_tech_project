#          'age',
#         'gender',
#         'monthlyIncome',
#         'essentialExpenses',
#         'personalSavings',
#         'availDownPay',
#         'existingLoan',
#         'locations'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("test.xlsx")

df_columns = ["datetime","age","gender","monthlyIncome","essentialExpense","personalSavings","availDownPay",\
"existingLoan","locations"]

df_new_columns = ["Year","Month","Date","Time","Minute","Seconds"]

date_time_hour=df["datetime"].str.split("-",expand=True)
date = date_time_hour[0] + "-" + date_time_hour[1] + "-" + date_time_hour[2]
time = date_time_hour[3]

df["date"] = date
df["time"] = time

input_date = input("Insert date of query (YYYY-MM-DD): ")
parameter = input("Insert parameter to query: ")

def hourly_traffic_by_date(input_date):
    data = df[df["date"]==input_date]
    pd.value_counts(data['time']).plot.bar()

def user_profile(parameter):
    print (df.groupby([parameter]).size().sort_values(ascending=False))
    
def correlation(inputA, inputB):
    df.plot(kind="scatter",x=inputA, y=inputB)


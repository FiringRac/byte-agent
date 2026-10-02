import pandas as pd
import numpy as np
from tools import inspect_data, filter_data, compare_data, clean_data, plot_data

df = pd.read_csv("data/employee.csv")
print(inspect_data(df))
print(filter_data(df, "City", "Delhi"))
print(compare_data(df, "mean", "City", "Salary"))
print(clean_data(df))
print(plot_data(df, "City", "Salary"))
print("hello world")
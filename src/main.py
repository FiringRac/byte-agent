import pandas as pd
import numpy as np
from tools import inspect_data

df = pd.read_csv("data/employee.csv")
print(inspect_data(df))

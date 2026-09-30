import pandas as pd
import numpy as np

def inspect_data(df):
    return {
        "rows" : len(df), 
        "columns" : list(df.columns),
        "datatypes" : df.dtypes.astype(str).to_dict(),
        "null values" : df.isna().sum().to_dict()
    }
    
def filter_data(df, column, value):
    return(df[df[column] == value])
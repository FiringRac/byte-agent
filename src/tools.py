import pandas as pd
import numpy as np

def inspect_data(df):
    #return dataset metadata to LLM
    return {
        "rows" : len(df), 
        "columns" : list(df.columns),
        "datatypes" : df.dtypes.astype(str).to_dict(),
        "null values" : df.isna().sum().to_dict()
    }
    
def filter_data(df, column, value):
    #return rows where the value in the specified column is equal to the value needed
    return(df[df[column] == value])

def compare_data(df, operation, group_by, column):
    #perform an aggregate function on one column grouped by another 
    group = df.groupby(group_by)[column]
    
    if operation == "sum":
        return group.sum()
    
    elif operation == "count":
        return group.count()
    
    elif operation == "min":
        return group.min()
    
    elif operation == "max":
        return group.max()
    
    elif operation == "mean":
        return group.mean()
    
    else:
        raise ValueError(f"Unsupported operation: {operation}")
    
def clean_data(df):
    #replaces missing numerical values with the median of the column, and missing text values with the most common value
    df = df.copy() #so we don't silently mess with the original data
    
    for x in df.columns:
        if df[x].isna().any():
            if df[x].dtype.kind in "biufc":
                df[x] = df[x].fillna(df[x].median())
            else:
                df[x] = df[x].fillna(df[x].mode()[0])
                
    return df

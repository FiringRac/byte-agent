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
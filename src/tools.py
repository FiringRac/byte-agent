import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from langchain_core.tools import tool

def create_tools(df):
    """create analysis tools that operate on the given dataframe"""
    
    @tool
    def inspect_data():
        """inspect the dataset and return its structure, data types and missing values."""
        return {
                "rows" : len(df), 
            "columns" : list(df.columns),
            "datatypes" : df.dtypes.astype(str).to_dict(),
            "null values" : df.isna().sum().to_dict()
        }
    

    @tool
    def filter_data(column: str, value: str):
        """"find rows where the value in the specified column is equal to the value needed"""
        result = df[df[column].astype(str) == value]
        return result.to_dict(orient = "records")

    @tool
    def compare_data(operation, group_by, column):
        """perform an aggregate function on one column grouped by another.""" 
        group = df.groupby(group_by)[column]
    
        if operation == "sum":
            result =  group.sum()
    
        elif operation == "count":
            result = group.count()
    
        elif operation == "min":
            result = group.min()
    
        elif operation == "max":
            result = group.max()
    
        elif operation == "mean":
            result = group.mean()
    
        else:
            raise ValueError(f"Unsupported operation: {operation}")
        
        return result.to_dict()
    
    return [inspect_data, filter_data, compare_data,]

def clean_data(df):
    """replaces missing numerical values with the median of the column, and missing text values with the most common value"""
    df = df.copy() #so we don't silently mess with the original data
    
    for x in df.columns:
        if df[x].isna().any():
            if df[x].dtype.kind in "biufc":
                df[x] = df[x].fillna(df[x].median())
            else:
                df[x] = df[x].fillna(df[x].mode()[0])
                
    return df

def plot_data(df, x, y, kind="bar"):
    """create a plot from two columns in the dataset and save it as an image."""
    ax = df.plot(x=x, y=y, kind=kind)
    
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig("plot.png")
    plt.close(fig)
    
    return "plot.png"
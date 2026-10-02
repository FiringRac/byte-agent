import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import create_tools

model = ChatGoogleGenerativeAI(
    model = "gemini-3.8-flash",
    temperature = 0
)

df = pd.read_csv("data/employee.csv")
tools = create_tools(df)

print("\n --- INSPECT ---")
print(tools[0].invoke({}))

print("\n --- FILTER ---")
print(tools[1].invoke({"column" : "City", "value" : "Delhi"}))

print("\n --- COMPARE ---")
print(tools[2].invoke({"group_by" : "City", "column" : "Salary", "operation" : "max"}))

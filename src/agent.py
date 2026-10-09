import pandas as pd
from tools import create_tools
from langchain_google_genai import ChatGoogleGenerativeAI
import json
from langchain_core.messages import HumanMessage, ToolMessage

print("1: creating model")
df = pd.read_csv("data/employee.csv")
tools = create_tools(df)

model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0
)

print("2: binding tools")

model_with_tools = model.bind_tools(tools)

print("3: asking LLM")

response = model_with_tools.invoke(
    "Inspect the data and tell me how many columns have the int or float data type"
)

#a small test
question = "Inspect the dataset and tell me how many columns have the int or float datatype."

messages = [
    HumanMessage(content=question),
    response
]

for tool_call in response.tool_calls:
    for tool in tools:
        if tool.name == tool_call["name"]:
            result = tool.invoke(tool_call["args"])

            messages.append(
                ToolMessage(
                    content=json.dumps(result),
                    tool_call_id=tool_call["id"]
                )
            )

final_response = model.invoke(messages)

print("\n--- FINAL ANSWER ---")
print(final_response.text)

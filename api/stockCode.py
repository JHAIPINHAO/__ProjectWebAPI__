from . import api1
import pandas as pd
import json

@api1.route("/stockcode")
def stockCode():
    code_dataFrame = pd.read_csv("api/CodeSearch.csv")
    code_dataFrame1 = code_dataFrame[['code','name']]
    all_list = code_dataFrame1.values.tolist()
    python_list = [{item[0]:item[1]} for item in all_list]
    return json.dumps(python_list,ensure_ascii=False)

@api1.route("/stockcode/<int:code>")
def stockName(code):
    code_dataFrame = pd.read_csv("api/CodeSearch.csv")
    code_dataFrame1 = code_dataFrame[['code','name']]
    try:
        name = code_dataFrame1.query('code==@code')['name'].values[0]
    except IndexError:
        return f"白癡!! 沒有{code}"
    return name
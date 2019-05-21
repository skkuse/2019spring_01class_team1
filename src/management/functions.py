import pandas as pd
import numpy as np

def excel_to_data(path):
    df = pd.read_excel(path, header=1)
    return [{k:v for k,v in m.items() if pd.notnull(v)} for m in df.to_dict(orient='rows')]
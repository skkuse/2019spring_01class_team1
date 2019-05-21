import pandas as pd
import numpy as np
import glob

def excel_to_data(path):
    filelist = glob.glob(path+"/*.xlsx")
    df = pd.read_excel(filelist[0], header=1)
    return [{k:v for k,v in m.items() if pd.notnull(v)} for m in df.to_dict(orient='rows')]
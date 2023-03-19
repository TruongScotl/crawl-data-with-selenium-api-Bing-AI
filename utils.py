# read, write, export file
import re
import pandas as pd
from collections import defaultdict

# def merge(dicts):
#     result = defaultdict(list)
#     for d in dicts:
#         for key, value in d.items():
#             result[key].extend(value)
#     return result

def concat_list(list):
    pass


def read_key(path)->str:
    f = open(path, "r")
    return str(f.read())



# check validation email
def check_email(email)->None:
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(re.fullmatch(regex, email)):
        return "Valid"
 
    else:
        return "Invalid"


# parsing email
def extract_email(text)->list:
    """
    input: text
    return: list of string email
    """
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
    return emails


#read data
def read_data(path, name_col)->list:
    df = pd.read_csv(path)
    ls_col = df[name_col].tolist()
    return ls_col
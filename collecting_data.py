import pandas as pd
import os
import csv
import glob
import datetime

def format_delivery_period(value):
    formats = [
    "%b-%Y",
    "%Y.%m",
    "%Y-%m",
]
    result = None
    for format in formats:
        try:
            result = datetime.datetime.strptime(value, format)
            break
        except ValueError:
            pass

    if result is None:
        raise ValueError(f"Unknown date format: {value}") 

    return datetime.datetime.strftime(result, "%Y-%m")

path = os.getcwd()
file_xls = os.listdir(path +'\Excel_files')

for f in file_xls:
    print(f"Processing {f}")

    xl_file = pd.read_excel(f'Excel_files\\{f}', 'FEUA')
    #the files are formatted in two different ways so need to account for that

    if isinstance(xl_file.iloc[0][0], str):
        xl_file.columns = xl_file.iloc[0]
        xl_file = xl_file.drop(0)
    else:
        xl_file.columns = xl_file.iloc[1]
        xl_file = xl_file.drop([0,1])

    xl_file = xl_file.rename({name: name.replace("\n", " ") for name in xl_file.columns}, axis="columns")
    try:
        xl_file["Improved Delivery Period"] = xl_file["Delivery Period"].apply(format_delivery_period)
    except TypeError:
        pass
    
    file_path = f'Saved_dataframes\\{f[:-5]}.csv'
    xl_file.to_csv(file_path, encoding='utf-8', index=False)

print('Done')
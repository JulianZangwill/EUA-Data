import pandas as pd
import os
import numpy as np

path = os.getcwd()
files = os.listdir(path +'\Saved_dataframes')
df_list = []
COLUMNS = ['Contract', 'Delivery Period', 'Contract Volume', 'Open Price',
       'High Price', 'Low Price', 'Last Price', 'Settlement Price',
       'Exchange Volume EUA', 'Exchange Traded Contracts',
       'Exchange Number of Trades', 'TradeReg Volume EUA',
       'TradeReg Traded Contracts', 'TradeReg Number of Trades',
       'Open Interest Contracts', 'Open Interest']
for f in files:
    df = pd.read_csv('Saved_dataframes\\'+f)
    df = df.set_index(df.columns[0])
    #df['Delivery Period'] = df['Delivery Period'].astype(str)
    #df['Delivery Period'] = df['Delivery Period'].str.replace('.','-')
    try:
        df['Delivery Period'] = df['Improved Delivery Period']
        df = df.drop('Improved Delivery Period', axis =1)
    except KeyError:
        pass
    df_list.append(df)

df_main = pd.concat(df_list) #combines all of the dfs to create one big list
df_main = df_main.dropna(how = 'all') #removes some of the empty rows
df_main['Trading Day'] = pd.to_datetime(df_main.index)

#Orders values by Trading day and Delivery period, then adds a column for the order the contracts are in
df_main = df_main.sort_values(['Trading Day','Delivery Period'])
df_main['Contract Number'] = df_main.groupby('Trading Day').cumcount()+1


df_main.to_csv(f'{path}\Modified_dataframes\EmissionCombined.csv', encoding='utf-8', index=False)

print('Done')
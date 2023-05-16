import matplotlib.pyplot as plt
import pandas as pd
import os
import create_multi
import datetime

#Purpose of this function would be to standardize movements across assets with different prices


#input series or df with ONLY Prices
def standardise(df):
    df_transformed = ((df-df.shift(1))/df.shift(1)).fillna(0)+1
    return df_transformed

if __name__ == '__main__':
    #############################################################################################################
    #Constructing example imput data
    number = 1
    df_file = pd.read_csv(f'Modified_dataframes\EmissionCombined.csv')
    df_file.index = pd.to_datetime(df_file['Trading Day'])
    df_contract_number = df_file[df_file['Contract Number'] == number][['Settlement Price', 'Delivery Period']]
    ##############################################################################################################
    df_price = df_contract_number['Settlement Price']
    df_percentage = standardise(df_price)
    df_cumulative = df_percentage.cumprod()

    print('Done')
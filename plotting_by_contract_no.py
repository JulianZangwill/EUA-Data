import matplotlib.pyplot as plt
import pandas as pd


contract_numbers = [1,2,3,5,10,15,20] # Represents the contract_number along the forward curve that we want to follow
for number in contract_numbers:
    df = pd.read_csv(f'Modified_dataframes\EmissionCombined.csv')
    df.index = pd.to_datetime(df['Trading Day'])
    df_contract_number = df[df['Contract Number'] == number]
    df_price = df_contract_number[['Settlement Price', 'Delivery Period']]

    fig = plt.figure()
    fig.set_figwidth(11)
    plt.margins(x=0.009)
    plt.plot(df_price['Settlement Price'], color = 'red')
    plt.ylabel('Price')
    plt.xlabel('Trading Day')
    plt.title(f'Price for contract {number} over time')
    plt.savefig(f'Graphs\Contract_No_{number}')
    plt.close()
print('Done')
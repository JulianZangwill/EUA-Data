import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(f'Modified_dataframes\EmissionCombined.csv')
df.index = pd.to_datetime(df['Trading Day'])

contract_numbers = range(1, 21) # Represents the contract_number along the forward curve that we want to follow

for number in contract_numbers:
    print(f'Plotting price and variation for contract #{number}')

    min_price = 0.01 # Prices <= this are replaced by None and show as data-gaps

    # select first contract as the spot value and remove bad values
    df_contract_one = df[df['Contract Number'] == 1]['Settlement Price'].copy() # copy needed to stop Pandas whinging
    df_contract_one[df_contract_one <= min_price] = None

    # select nth contract and remove bad values
    df_contract_number = df[df['Contract Number'] == number]['Settlement Price'].copy()
    df_contract_number[df_contract_number <= min_price] = None

    # reindex to create gaps where there is missing data
    df_contract_number = df_contract_number.reindex(df_contract_one.index)
    
    # combine the two series to make new variation curve
    df_variation = df_contract_number/df_contract_one - 1

    # plot the two curves
    plt.margins(x=0.009)

    fig, ax1 = plt.subplots()
    fig.set_figwidth(11)
    ax1.set_title(f'Price for contract {number} over time')
    ax1.set_xlabel('Trading Day')
    ax2 = ax1.twinx()

    color = 'red'
    ax1.plot(df_contract_number, color=color)
    ax1.set_ylabel('Settlement Price', color=color)
    ax1.tick_params(axis='y', colors=color)

    color = 'blue'
    ax2.plot(df_variation, color=color)
    ax2.set_ylabel('Variation From Spot', color=color)
    ax2.tick_params(axis='y', colors=color)

    plt.savefig(f'Graphs\Variation_Contract_No_{number}')
    plt.close()

print('Done')
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import create_multi

def format_date(x, pos=None):
    '''Format dates for x and y axis'''
    return matplotlib.dates.num2date(x).strftime('%Y-%m')

df = pd.read_csv(f'Modified_dataframes\EmissionCombined.csv')
multi = create_multi.create_multi(df)
dates = multi.index.get_level_values(0)
dates = dates.drop_duplicates()
# There are many! Just choose a few
dates = dates[::10]
x = []
y = []
z = []
for date in dates:
    print(f'Adding data from {date}...')
    specific_frame = multi.loc[multi.index.get_level_values(0)==date][['Settlement Price', 'Contract Number']].unstack(level=0).sort_index()
    specific_frame.index = pd.to_datetime(specific_frame.index)

    # Translate dates to numbers
    date_datetime = datetime.datetime.strptime(date, '%Y-%m-%d')
    date_num = matplotlib.dates.date2num(date_datetime)
    day_nums = matplotlib.dates.date2num(specific_frame.index)
    settlement_prices = specific_frame['Settlement Price'].values.flatten()
    x.extend([date_num]*len(day_nums))
    y.extend(day_nums)
    z.extend(settlement_prices)

# Plot the data
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True, cmap=matplotlib.cm.coolwarm)

# Format the axes
ax.w_xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(format_date))
ax.set_xlabel('Trading Day')
ax.w_yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(format_date))
ax.set_ylabel('Delivery Period')

# Add title and save
print(f'Plotting forward curves from {dates[0]} to {dates[-1]}')
plt.title(f'Forward curves from {dates[0]} to {dates[-1]}')
plt.savefig(f'Graphs\Forward_Curves_{dates[0]}-{dates[-1]}.png', bbox_inches='tight')
plt.show()
plt.close()

print('Done')
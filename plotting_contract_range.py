import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import pandas as pd

# Maximum contract number per trading day
df = pd.read_csv(f'Modified_dataframes\EmissionCombined.csv')
df['Trading Day'] = pd.to_datetime(df['Trading Day'])
df = df.set_index('Trading Day')
df_range = df.groupby('Trading Day')['Contract Number'].max()

# Plot it as vertical lines
fig = plt.figure()
fig.set_figwidth(11)
plt.margins(x=0.009)
plt.title('Range of Contract Numbers')
plt.xlabel('Trading Date')
plt.ylabel('Contract Numbers')
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=20, integer=True))
plt.vlines(df_range.index, 0, df_range, color='purple')
plt.savefig(f'Graphs\Contract_Number_Range')

print('Done')
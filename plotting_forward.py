import matplotlib.pyplot as plt
import pandas as pd
import os
import create_multi
import datetime

#input date wanted here
#

df = pd.read_csv(f'Modified_dataframes\EmissionCombined.csv')
multi = create_multi.create_multi(df)
dates = multi.index.get_level_values(0)
dates = dates.drop_duplicates()
# There are many! Just choose a few
dates = [
    '2010-06-30',
    '2011-07-12',
    '2022-10-13',
]
for date in dates:
    print(f'Plotting {date}')
    specific_frame = multi.loc[multi.index.get_level_values(0)==date][['Settlement Price', 'Contract Number']].unstack(level=0).sort_index()

    contract_count = len(specific_frame.index)

    specific_frame.index = pd.to_datetime(specific_frame.index)
    ##contract_frame = specific_frame['Contract Number']

    try:
        fig = plt.figure()

        # Choose parameters to suit the maximum date range:
        annotation_size = 6     # Font size of annotations
        fig.set_figwidth(11)    # Choose a width that makes the annotations legible
        plt.margins(x=0.009)    # Bare minimum margin to just see the first and last annotation

        plt.plot(specific_frame['Settlement Price'], color = 'green', marker='o')
        plt.ylabel('Price')
        plt.xlabel('Delivery Period')

        # Locate mid-range (assuming monotonic...)
        first = specific_frame['Settlement Price'].iat[0, -1]
        last = specific_frame['Settlement Price'].iat[-1, -1]
        range = last - first
        mid = (first + last)/2
        annotation_offset = range/30

        for day, values in specific_frame.iterrows():
            y = values[0]
            n = values[1]

            # Flip annotation position in top half of plot
            if y < mid:
                v_offset = annotation_offset
                v_alignment = 'bottom'
            else:
                v_offset = -annotation_offset
                v_alignment = 'top'

            # Add the annotation
            plt.annotate(
                f'{n:n} ({day:%Y-%m})',   # Text
                (day, y + v_offset),      # Position
                rotation=90,              # Orientation
                ha='center',              # Horizontal Alignment
                va=v_alignment,           # Vertical Alignment
                fontsize=annotation_size, # Font Size
            )

        plt.figtext(0.2,0.8, f'No. Contracts: {contract_count}')
        plt.title(f'Forward curve on {date}')

        # Save plot with the minimum of white-space
        plt.savefig(f'Graphs\Forward_Curve_{date}', bbox_inches='tight')
        plt.close()
    except ZeroDivisionError:
        print('Not a Trading Day')  #need to select a different date

print('Done')
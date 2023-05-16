import pandas as pd
def create_multi(df):
    reset_df = df.reset_index()
    multi = reset_df.set_index([reset_df['Trading Day'],reset_df['Delivery Period']])
    return multi
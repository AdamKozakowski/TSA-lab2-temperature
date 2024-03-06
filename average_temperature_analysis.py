import pandas as pd
import numpy as np

#Get the average temperature data for St. Louis, Missouri from NOOA website. Import dataset
monthly_average_temperature_df= pd.read_csv('monthly_average_temperature_data.csv')

#Locate missing values and change them to nan.
monthly_average_temperature_df.loc[-99, 'Value'] = np.nan
monthly_average_temperature_df.loc[-99, 'Anomaly'] = np.nan

#Use the interpolate function to put a value in the Nan’s place
monthly_average_temperature_df = monthly_average_temperature_df.interpolate()

# Convert the index to datetime format
monthly_average_temperature_df.to_datetime(monthly_average_temperature_df['Date'])
monthly_average_temperature_df.set_index('Date',inplace=True)
print(monthly_average_temperature_df.head())
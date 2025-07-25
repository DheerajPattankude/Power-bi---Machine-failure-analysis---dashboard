import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\dhiru\Downloads\ai4i+2020+predictive+maintenance+dataset.zip')
print(df)

df['temperature deff. [k]'] = df['Process temperature [K]'] - df['Air temperature [K]']
df['power'] = df['Torque [Nm]'] * df['Rotational speed [rpm]']
df['wear_rate'] = df['Tool wear [min]'] / df['Rotational speed [rpm]']
df['Torque_per_rpm'] = df['Torque [Nm]'] / df['Rotational speed [rpm]']
column_name = ['Product ID','temperature deff. [k]','power','wear_rate','Torque_per_rpm','Machine failure']
new_df = df[column_name]
print(new_df)
#new_df.to_csv('transform_data_for_analysis.csv')
column_name2 =['Machine failure','TWF','HDF','PWF','OSF','RNF']
corr_df = df[column_name2]
print(corr_df.corr())

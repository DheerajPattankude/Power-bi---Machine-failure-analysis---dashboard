import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\dhiru\Downloads\predictive+maintenance+dataset\Machine failure data with parameters.csv')
print(df)

df.info() # no null value found and all dada type are righ
df.drop_duplicates()#remove du
df.dropna()
df.describe(include='all') # 

#rate of falure and corect Machine manufacture
print(df['Machine failure'].value_counts())
total_failure = (df['Machine failure'] == 1).sum()
total_correct = (df['Machine failure'] == 0).sum()
total_number_of_machine = df['Machine failure'].count()
rate_of_failure = (total_failure/total_number_of_machine)*100
print(f"rate of failure : {rate_of_failure}%")
print(f"rate of effective manufacture : {100-(rate_of_failure)}%")

# rate of falure by each type of Machine
count_type = df.groupby(['Type','Machine failure']).size()
#print (count_type)
count_type_H =(df['Type'] == 'H').sum()
count_type_L =(df['Type'] == 'L').sum()
count_type_M =(df['Type'] == 'M').sum()
print(f"rate_of_type_H_failure : {(21/count_type_H)*100}%")
print(f"rate_of_type_L_failure: {(235/count_type_L)*100}%")
print(f"rate_of_type_M_failure: {(83/count_type_M)*100}%")

y=df['Machine failure'].sum()

plt.subplot(1,2,1)
x=df['Type']
plt.hist(x, y)
plt.title('total coynt by type')

plt.subplot(1,2,2)
data=df.groupby(['Type','Machine failure']).size()
mylabels=['Machine H','H failure','Machine L','L failure','Machine M','M failure']
plt.pie(data,labels=mylabels)
plt.title('data distrubition')
plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## read from csv file
data=pd.read_csv('data.csv')


### Q 1
income_data=data.groupby('Name')[['January income','February income','March income',
                           'April income','May income','June income',
                           'July income','August income','September income',
                           'October income','November income','December income']].mean()
bar_Name=income_data.index.to_list()
values=income_data.mean(axis=1).values
plt.figure(figsize=(15,10))
plt.bar(bar_Name,values)
plt.xlabel("Name")
plt.ylabel("Average Income")
plt.title("Average Income per Person for Qustion 1")
plt.show()


### Q 2
# find x values for line plot that is 12 months
months=np.arange(1,len(income_data.columns.to_list())+1)

# make arrar from 12 incoming for each person 
income_List=[]
for i in range(0,5):
    income_List.append(income_data.iloc[i].values)    
income_List=np.array(income_List)

# line plot
plt.figure(figsize=(15,10))
for i in range(0,5):
    plt.plot(months,income_List[i])
plt.xlabel("Month")
plt.ylabel("Income")
plt.title("Trend of Income Change for Qustion 2")
plt.legend(bar_Name)
plt.show()

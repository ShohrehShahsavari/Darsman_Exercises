import numpy as np
import pandas as pd

## read from csv file
data=pd.read_csv('e1.csv')
# print(data['Age'])

### change noisy data for age
for i in range(len(data['Age'])):
    temp=''
    for j in range(len(data['Age'][i])):
        if data['Age'][i][j]!=' ':
            temp+=data['Age'][i][j]
    data['Age'][i]=temp

### change column type
data['Age']=data['Age'].astype(int)

### Q 1  mean and mode for Age and Weight
mean=data[['Age','Weight']].mean()
median=data[['Age','Weight']].median()
print(f'Age mean:{mean[0]}\t\tAge median:{median[0]}\nWeight mean:{mean[1]}\tAge median:{median[1]}')
print(80*'*')

## Q 2 mode for Height Gender Education
Height_mode=data['Height'].mode()[0]
Gender_mode=data['Gender'].mode()[0]
Education_mode=data['Education'].mode()[0]
## mode=data[['Height','Gender','Education']].mode()
## print(mode)
print(f'Height mode is: {Height_mode}\nGender mode is: {Gender_mode}\nEducation mode is: {Education_mode}')
print(80*'*')

## Q 3 Range for Age Height Weight
Age_range=np.ptp(data['Age'])
Height_range=np.ptp(data['Height'])
Weight_range=np.ptp(data['Weight'])
print(f'Age range is: {Age_range}\nHeight range is: {Height_range}\nWeight range is: {Weight_range}')
print(80*'*')

## Q 4 Variance and std for Age Height Weight
variance=np.var(data[['Age','Height','Weight']])
std_dev=np.std(data[['Age','Height','Weight']])
print(variance)
print(std_dev)
print(80*'*')

## Q 5 quartiles for Age Height Weight
Age_quartiles=np.percentile(data['Age'],[25,50,75])
Height_quartiles=np.percentile(data['Height'],[25,50,75])
Weight_quartiles=np.percentile(data['Weight'],[25,50,75])
print(f'Age quartiles is: {Age_quartiles}\nHeight quartiles is: {Height_quartiles}\nWeight quartiles is: {Weight_quartiles}')
print(80*'*')

## Q6 IQR for Age Height Weight
Age_IQR=Age_quartiles[2]-Age_quartiles[0]
Height_IQR=Height_quartiles[2]-Height_quartiles[0]
Weight_IQR=Weight_quartiles[2]-Weight_quartiles[0]
print(f'Age IQR is: {Age_IQR}\nHeight IQR is: {Height_IQR}\nWeight IQR is: {Weight_IQR}')
print(80*'*')


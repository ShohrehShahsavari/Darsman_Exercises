import numpy as np
###################### extract information from text #############################
import re
with open('3_3353_3a46efa5-c161-4d38-8f3a-6a311c3c8b25.txt','r') as file1:
    strfile=file1.read()
    list_of_2019_raining=re.findall('(\d+\.\d|\d{2})',strfile)

with open('3_3353_188e1827-b454-4f54-8a79-0cad444dafb9.txt','r') as file1:
    strfile=file1.read()
    list_of_2020_raining=re.findall('(\d+\.\d|\d{2})',strfile)
        
with open('3_3353_c9087d6f-cbca-43b8-9f14-c36d1c02d92c.txt','r') as file1:
    strfile=file1.read()
    list_of_2021_raining=re.findall('(\d+\.\d|\d{2})',strfile)

##################################################################################
# creat arrays , reshaped and retype them from previous lists
arr1=np.array(list_of_2019_raining)
arr2=np.array(list_of_2020_raining)
arr3=np.array(list_of_2021_raining)

newArr1=arr1.astype('f')
newArr2=arr2.astype('f')
newArr3=arr3.astype('f')

arr2019=newArr1.reshape(3,5)
arr2020=newArr2.reshape(3,5)
arr2021=newArr3.reshape(3,5)

#################################### Avarage #######################################
# creat average list for each months
avarage_for_2019_raining=[]
avarage_for_2020_raining=[]
avarage_for_2021_raining=[]
for i in range(len(arr2019)):
    avarage_for_2019_raining.append(np.average(arr2019[i]))
for i in range(len(arr2020)):
    avarage_for_2020_raining.append(np.average(arr2020[i]))
for i in range(len(arr2021)):
    avarage_for_2021_raining.append(np.average(arr2021[i]))    

####################################################################################
# creat total avarage raining array with years
'''
[
    [2019   23     23.6    30.57]
    [2020   28.72   30.52   35.40]
    [2021   43.38   42.78   46.38]
]
'''
yeararr=np.array([2019,2020,2021])
avgarr1=np.array(avarage_for_2019_raining)
avgarr2=np.array(avarage_for_2020_raining)
avgarr3=np.array(avarage_for_2021_raining)
total_avg_arr=np.dstack((yeararr,avgarr1,avgarr2,avgarr3))
print('Totall avarage rain array based on years: ')
print(total_avg_arr)
#print(total_avg_arr.shape)

####################################################################################
### find maximum raining:
max=0
for i in range(0,1):
    for j in range(0,3):
        for k in range(0,4):
            if total_avg_arr[i][j][k]!=2019 and total_avg_arr[i][j][k]!=2020 and total_avg_arr[i][j][k]!=2021:
                if total_avg_arr[i][j][k]>max:
                    max=total_avg_arr[i][j][k]
print(f'maximum raining is: {max}')
x=np.where(total_avg_arr==max)
#### find month and year for max rain:
if x[1]==0:
    year=2019
if x[1]==1:
    year=2020
if x[1]==2:
    year=2021
print(f'year of highest rain is: {year}')
print(f'month of highest rain is: {x[2][0]}')
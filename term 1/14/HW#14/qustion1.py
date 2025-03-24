import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

################## read information from file #############################

df_product_A=pd.read_csv('product_A.csv')
df_product_B=pd.read_csv('product_B.csv')
df_product_C=pd.read_csv('product_C.csv')

################## convert None to zero ###################################

new_df_product_A=df_product_A.fillna(value=0)
#print(new_df_product_A)

################## find Maximum ###########################################
frames = [df_product_A, df_product_B, df_product_C]
result = pd.concat(frames)
df_max=result.groupby(['Code']).max()
print('Maximum View,Like,Order for all product:')
print(df_max)
################### bar plot ##############################################
fig, axes = plt.subplots(nrows=1, ncols=3)
df_max.plot(y='View',kind='bar',subplots=True,ax=axes[0])
df_max.plot(y='Like',kind='bar',subplots=True,ax=axes[1])
df_max.plot(y='Order',kind='bar',subplots=True,ax=axes[2])
plt.show()

print('maximum of View is: ')
print(df_max[['View']].max()[0])

print('maximum of Like is: ')
print(df_max[['Like']].max()[0])

print('maximum of Order is: ')
print(df_max[['Order']].max()[0])
#################### Max Order plot #######################################

x=new_df_product_A["Day"]
y=new_df_product_A["Order"]
plt.subplot(1,3,1)
plt.plot(x,y,'o-')
plt.title('A_Product')
plt.xlabel('Day')

x=df_product_B["Day"]
y=df_product_B["Order"]
plt.subplot(1,3,2)
plt.plot(x,y,'o-')
plt.title('B_Product')
plt.xlabel('Day')

x=df_product_C["Day"]
y=df_product_C["Order"]
plt.subplot(1,3,3)
plt.plot(x,y,'o-')
plt.title('C_Product')
plt.xlabel('Day')
plt.show()
from extraction import *
from transforms import *
from loads import *
import pandas as pd

def printData(data):
    print(80*"-")
    print(data)
    print(80*'*')
data=extractt_from_csv("orders.csv")
#printData(data)

# print(data.info())

# drop all NAN's record
data=drop_records_all_nans(data)
# printData(data)

#remove noisy data
data=fill_noisy_data(data)
# printData(data)

# change column type
data=change_type_columns(data,['CustomerName','Product','Quantity','PurchaseAmount','Color','Weight'],
                         ['str','str','int','float','str','float'])
# printData(data)


# Convert the date column to a datetime object.
date=change_column_to_date(data,'PurchaseDate')
# printData(data)

# fill NANs
data=fillna(data)
# printData(data)

# one hot encoder
data=one_hot_encoding(data,['IsAvailable'])
# printData(data)

# lable coding
data=lable_encoding(data,['Color'])
# printData(data)

# گسسته سازی
k_bins_discretizer(data,columns=['Quantity'])
# printData(data)


# remove outlier data
# check_outlier_column(data,['Weight','PurchaseAmount'])
data=remove_weight_outlier(data,min_w=1,max_w=150)
# printData(data)
data=remove_PurchaseAmount_outlier(data,min_A=0,max_A=500000)
# printData(data)

# drop column
data=drop_columns(data,['CustomerName'])
# printData(data)

# Normalization
data=min_max_scaler(data,['Quantity','PurchaseAmount','Color','Weight','IsAvailable_No','IsAvailable_Yes'])
# printData(data)

loads(data,'targetFile.csv')
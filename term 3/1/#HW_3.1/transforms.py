import pandas as pd
import numpy as np

# drop all NAN's record
def drop_records_all_nans(data):
    return data.dropna(how="all",axis=0)

#remove noisy data
def fill_noisy_data(data):
    #data.loc[data.PurchaseAmount.astype('str').str.islower(),'PurchaseAmount']= data.loc[data.PurchaseAmount.astype('str').str.isnumeric(),'PurchaseAmount'].median()
    data.loc[~data['PurchaseAmount'].astype('str').str.isnumeric(),'PurchaseAmount']=np.nan
    return data

# change column type
def change_type_columns(data,columns,types):
    df=pd.DataFrame(data)
    for i in range(len(columns)):
        df[columns[i]]=df[columns[i]].astype(types[i])
    return df

# Convert the date column to a datetime object.
def change_column_to_date(data,column):
    data[column] = pd.to_datetime(data[column])
    return data

# fill NANs
def fillna(data):
    data.fillna(value={
        'PurchaseDate':data.PurchaseDate.median(),
        'Product':data.Product.mode()[0],
        'Quantity':data.Quantity.mean(),
        'PurchaseAmount':data.PurchaseAmount.mean(),
        'Color':data.Color.mode()[0],
        'IsAvailable':data.IsAvailable.mode()[0],
        'Weight':round(data.Weight.mean()) 
    },inplace=True)
    return data


# one hot encoder
def one_hot_encoding(data,columns):
    return pd.get_dummies(data,columns=columns)

# lable Encoding
from sklearn.preprocessing import LabelEncoder
def lable_encoding(data,columns):
    le=LabelEncoder()
    for col in columns:
        data[col]=le.fit_transform(data[col])
    return data

# گسسته سازی
from sklearn.preprocessing import KBinsDiscretizer
def k_bins_discretizer(data,columns):
    dis=KBinsDiscretizer(n_bins=4,encode='ordinal',strategy='uniform')
    for col in columns:
        data[col]=dis.fit_transform(data[[col]])
    return data

# remove outlier data
import plotly.express as px
def check_outlier_column(data,columns):
    fig=px.box(data,columns)
    fig.show()

def remove_weight_outlier(data,min_w,max_w):
    df=pd.DataFrame(data)
    data=df[(df['Weight']>=min_w) & (df['Weight']<=max_w)]
    return data

def remove_PurchaseAmount_outlier(data,min_A,max_A):
    df=pd.DataFrame(data)
    data=df[(df['PurchaseAmount']>=min_A) & (df['PurchaseAmount']<max_A)]
    return data

# drop column
def drop_columns(data,columns):
    for col in columns:
        data.drop(col,axis=1,inplace=True)
    return data

# drop column
def drop_columns(data,columns):
    for col in columns:
        data.drop(col,axis=1,inplace=True)
    return data

# Normalization
from sklearn.preprocessing import MinMaxScaler
def min_max_scaler(data,columns):
    scaler=MinMaxScaler()
    data[columns]=scaler.fit_transform(data[columns])
    return data





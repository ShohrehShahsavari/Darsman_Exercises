
# import pandas as pd

# # Load the data from a CSV file.
# data = pd.read_csv('data.csv')

# # Drop the id column.
# data = data.drop('id', axis=1)

# # Convert the date column to a datetime object.
# data['date'] = pd.to_datetime(data['date'])

# # Fill in the missing values in the price column with the mean.
# data['price'] = data['price'].fillna(data['price'].mean())

# # Save the transformed data to a new CSV file.
# data.to_csv('transformed_data.csv')



# import pandas as pd

# # Load the data from a CSV file.
# data = pd.read_csv('data.csv')

# # Remove duplicate rows.
# data = data.drop_duplicates()

# # Fix typos in the name column.
# data['name'] = data['name'].replace('John Doe', 'John Smith')

# # Convert the date column to a datetime object.
# data['date'] = pd.to_datetime(data['date'])



# import pandas as pd

# # Load the data from a CSV file.
# data = pd.read_csv('data.csv')

# # Convert the gender column to a numerical value.
# data['gender'] = data['gender'].map({'male': 0, 'female': 1})

# # Scale the price column so that it is between 0 and 1.
# data['price'] = data['price'] / data['price'].max()


# import pandas as pd

# # Load the customer data from a CSV file.
# customer_data = pd.read_csv('customer_data.csv')

# # Load the sales data from a CSV file.
# sales_data = pd.read_csv('sales_data.csv')

# # Combine the customer data and sales data into a single DataFrame.
# combined_data = pd.merge(customer_data, sales_data, on='customer_id')



import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def min_max_scaler(data, columns):
    """Normalizes the data in the specified columns using min-max scaling."""
    scaler = MinMaxScaler()
    data[columns] = scaler.fit_transform(data[columns])
    return data

data = pd.DataFrame({'Quantity': [1, 2, 3],
                    'PurchaseAmount': [100, 200, 300],
                    'Color': ['Red', 'Blue', 'Green'],
                    'Weight': [10, 20, 30],
                    'IsAvailable_No': [0, 0, 1],
                    'IsAvailable_Yes': [1, 1, 0]})

data = min_max_scaler(data, ['Quantity', 'PurchaseAmount', 'Weight'])

print(data)
# str='23 45 2'
# mainstr=''
# for ch in str:
#     if ch!=' ':
#         mainstr+=ch
# print(mainstr)


# import pandas as pd

# # Create a DataFrame
# df = pd.DataFrame({'A': [1, 1, 2, 2, 3], 'B': [3, 2, 2, 3, 1]})

# # Get the mode of the two columns
# mode = df[['A', 'B']].mode()

# # Print the mode
# print(mode)


import pandas as pd
# Create a dataframe
# df = pd.DataFrame({'Name': ['John', 'Jane', 'Peter', 'Mary', 'David'],
#                    'June income': [1000, 2000, 3000, 4000, 5000],
#                    'September income': [6000, 7000, 8000, 9000, 10000],
#                    'November income': [11000, 12000, 13000, 14000, 15000]})
# print(df)
# # Group the dataframe by name and calculate the mean of salary for each month
# monthly_income_mean = df.groupby('Name')['June income', 'September income', 'November income'].mean()
# # Print the results
# print(monthly_income_mean)

############## Q 1
# import pandas as pd
# import matplotlib.pyplot as plt

# # Create a DataFrame
# df = pd.DataFrame({
#     "Name": ["Ali", "Ahmad", "Sara", "Reza", "Narges"],
#     "Age": [25, 30, 22, 35, 28],
#     "Height": [174, 191, 168, 178, 159],
#     "Weight": ["69", "88", "65", "94", "57"],
#     "Gender": ["Male", "Male", "Female", "Male", "Female"],
#     "Hobby": ["Music", "Sports", "Movies", "History", "Travel"],
#     "City": ["Tehran", "Shiraz", "Esfahan", "Tabriz", "Mashhad"],
#     "Education": ["Bachelor", "Master", "PhD", "Bachelor", "Master"],
#     "MaritalStatus": ["Single", "Married", "Single", "Married", "Single"],
#     "Number of children": [0, 2, 1, 1, 0],
#     "January income": [1250, 2400, 1200, 2900, 1950],
#     "February income": [1250, 2400, 1800, 2900, 1950],
#     "March income": [1250, 2400, 1800, 2900, 1950],
#     "April income": [1800, 2400, 1800, 3100, 2400],
#     "May income": [1800, 2400, 1950, 2800, 2400],
#     "June income": [1800, 2650, 2800, 2800, 2400],
#     "July income": [1800, 2650, 2200, 2600, 2600],
#     "August income": [1800, 2650, 2300, 2600, 4300],
#     "September income": [1800, 2650, 2300, 2600, 3100],
#     "October income": [2100, 2300, 2450, 2400, 4700],
#     "November income": [2100, 2200, 2450, 2300, 1520],
#     "December income": [2500, 2700, None, 2300, 1600]
# })
# #print(df)
# # Group the DataFrame by name and calculate the mean income
# average_income_per_person = df.groupby('Name')['January income'].mean()
# #print(average_income_per_person)
# # Get bar names
# bar_names = average_income_per_person.index.to_list()

# # Get maximum bar name string lengths
# max_name_length = 0
# for name in bar_names:
#   max_name_length = max(max_name_length, len(name))

# # Get total number of bars
# n_bars = len(bar_names)

# # Rotate x axis labels if number of bars and max_name_length are large
# if n_bars * max_name_length >= 50:
#   if n_bars >= 20:
#     plt.xticks(rotation=90)
#   else:
#     plt.xticks(rotation=45)

# # Create a bar chart of the average income per person
# plt.bar(average_income_per_person.index, average_income_per_person.values)
# plt.xlabel("Name")
# plt.ylabel("Average Income")
# plt.title("Average Income per Person in the DataFrame")
# plt.show()


################ Q 2
import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    "Name": ["Ali", "Ahmad", "Sara", "Reza", "Narges"],
    "Month": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Income": [1250, 1250, 1200, 2900, 1950, 2800, 2600, 2600, 2600, 2400, 1520, 1600]
})

print(df)
## Group the DataFrame by name and calculate the monthly income
# monthly_income = df.groupby('Name')['Income'].agg(lambda x: x.tolist())

# # Create a line chart of monthly income for each individual
# plt.figure(figsize=(10, 6))
# for name, group in monthly_income.items():
#     plt.plot(group.index, group, label=name)

# plt.xlabel("Month")
# plt.ylabel("Income")
# plt.title("Trend of Income Change for Each Individual")
# plt.legend()
# plt.show()


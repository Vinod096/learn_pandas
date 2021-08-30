import pandas as pd

items_1 = [{'bike': 20, 'watches': 30, 'pants': 20, 'glasses': 15, 'shirts': 50},
           {'bike': 15, 'watches': 40, 'pants': 50, 'glasses': 45, 'pens': 10},
           {'bike': 25, 'watches': 60, 'pants': 50, 'glasses': 95, 'books': 40}]

items_1 = pd.DataFrame(items_1, index=['store_1', 'store_2', 'store_3'])

print("New dataframe : \n", items_1)

null_values =items_1.isnull() #To show null valus in boolean

print("Null Values (Boolean Values)  : \n ", null_values)

null_values_1 = items_1.isnull().sum() #To show null values is each row and column

print("Null Values in each Column : \n ", null_values_1)

null_values_2 = items_1.isnull().sum().sum() # Addition of total null values in a dataframe

print("Total Null values in Data Frame : \n",null_values_2)

print("Total number of Non Null value in Data Frame : \n",items_1.count())
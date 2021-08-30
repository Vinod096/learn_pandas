import pandas as pd

items_1 = [{'bike': 20, 'watches': 30, 'pants': 20, 'glasses': 15, 'shirts': 50},
           {'bike': 15, 'watches': 40, 'pants': 50, 'glasses': 45, 'pens': 10},
           {'bike': 25, 'watches': 60, 'pants': 50, 'glasses': 95, 'books': 40}]

items_1 = pd.DataFrame(items_1, index=['store_1', 'store_2', 'store_3'])

print("New dataframe : \n", items_1)

new_values = items_1.fillna(0)

print("New values : \n",new_values)

new_values_1 = items_1.fillna(method = 'ffill', axis= 0) #Forward filling method

print("Forward Filling  : \n",new_values_1)

new_values_2 = items_1.fillna(method='backfill', axis=1) #Backward filling method

print("Backward Filling  : \n", new_values_1)

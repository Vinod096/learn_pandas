import pandas as pd

groceries = pd.Series(data=[30, 6, 'yes', 'no'], index=['eggs', 'apples', 'milk', 'bread'])

print("Groceries : \n", groceries)

print("The data in groceries : ", groceries.values)
print("The data in groceries : ", groceries.index)


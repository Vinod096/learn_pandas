import pandas as pd

x = pd.Series(data=[30, 6, 'yes', 'no'], index=['eggs', 'apples', 'milk','bread'])

print("Groceries : \n", x)

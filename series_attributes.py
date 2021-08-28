import pandas as pd

groceries = pd.Series(data=[30, 6, 'yes', 'no'], index=['eggs', 'apples', 'milk', 'bread'])

print("Groceries : \n", groceries)

print("Groceries has shape : ", groceries.shape)

print("Groceries has dmensions : ", groceries.ndim)

print("Groceries has total of ", groceries.size,'elements')


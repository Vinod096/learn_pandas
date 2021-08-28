import pandas as pd

items = [{'bikes' : 20, 'pants' : 30, 'watches' : 35 }, {'watches': 10,'glasses' : 50, 'bikes' : 15, 'pants' : 5}]

store_items = pd.DataFrame(items, index = ['store 1','store 2'])

print(store_items)

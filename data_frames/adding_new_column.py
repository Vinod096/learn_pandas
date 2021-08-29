import pandas as pd

items = [{'bikes': 20, 'pants': 30, 'watches': 35}, {
    'watches': 10, 'glasses': 50, 'bikes': 15, 'pants': 5}]

store_items = pd.DataFrame(items, index=['store 1', 'store 2'])

print("store_items : \n", store_items)

new_items = [{'bikes': 30, 'pants': 40, 'watches': 50, 'glasses': 60}]

new_store = pd.DataFrame(new_items, index=['store 3'])

#print("New Items : ",new_items)

store_items = store_items.append(new_store)

print("New Store : \n", store_items)

store_items['new_watches'] = store_items['watches'][1:]

print("New store items : \n",store_items)

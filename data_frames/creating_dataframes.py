import pandas as pd

items = {'Bob': pd.Series(data=[245, 25, 55], index=['bike', 'pants', 'watch']),
         'Alice': pd.Series(data=[40, 110, 500, 45], index=['book', 'glasses', 'bike', 'pants'])}

shopping_carts = pd.DataFrame(items)
print("Shopping Cart : \n", shopping_carts)

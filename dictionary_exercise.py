prices = {"bananas": 4, "apple": 2, "orange": 1.5, "pear": 3, }


compare_item, compare_price = prices.items()[0], prices.items()[0][1]

for item, number in prices():

    print item

# >>> prices.items()
# [('orange', 1.5), ('pear', 3), ('banana', 4), ('apple', 2)]
# >>> prices.keys()
# ['orange', 'pear', 'banana', 'apple']
# >>> prices.values()
# [1.5, 3, 4, 2]
# >>> prices.items()[0]
# ('orange', 1.5)
# >>> prices.items()[0][0]
# 'orange'
# >>> prices.items()[0][1]
# 1.5
# >>> lgst_val = prices.items()[0][1]
# >>> lst_val
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'lst_val' is not defined
# >>> lgst_val
# 1.5

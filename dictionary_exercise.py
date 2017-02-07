prices = {"bananas": 4, "apple": 2, "orange": 1.5, "pear": 3, }


compare_item, compare_price = prices.items()[0], prices.items()[0][1]

for item, number in prices():

    print item

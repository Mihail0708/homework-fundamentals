budget = float(input())
price_1kg_flour = float(input())
price_1pack_eggs = price_1kg_flour * 0.75
price_1l_milk = price_1kg_flour * 1.25
bread_price = (price_1l_milk/4) + price_1pack_eggs + price_1kg_flour
loaves = 0
bread = 0
colored_eggs = 0
total = 0
while budget > 0:
    if budget < bread_price:
        break
    loaves += 1
    colored_eggs += 3
    bread += 1
    if bread % 3 == 0:
        colored_eggs -= loaves - 2
    budget -= bread_price
    total += bread_price


print(f'You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')

quantity = int(input())
days_to_christmas = int(input())
points = 0
price = 0
days = 0
while days_to_christmas > 0:
    days += 1

    if days % 11 == 0:
        quantity += 2
    if days % 2 == 0:
        price += 2 * quantity
        points += 5
    if days % 3 == 0:
        price += 8 * quantity
        points += 13
    if days % 5 == 0:
        price += 15 * quantity
        points += 17
        if days % 3 == 0:
            points += 30
    if days % 10 == 0:
        points -= 20
        price += 23
    days_to_christmas -= 1
if days % 10 == 0:
    points -= 30
print(f'Total cost: {price}')
print(f'Total spirit: {points}')

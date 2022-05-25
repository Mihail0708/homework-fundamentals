orders = int(input())
total = 0
for i in range(orders):
    capsule_price = float(input())
    days = int(input())
    quantity_per_day = int(input())
    if capsule_price < 0.01 or capsule_price > 100.00 \
        or days < 1 or days > 31 \
        or quantity_per_day < 1 or quantity_per_day > 2000:
        continue
    total_today = capsule_price * days * quantity_per_day
    total += total_today
    print(f'The price for the coffee is: ${total_today:.2f}')
print(f'Total: ${total:.2f}')
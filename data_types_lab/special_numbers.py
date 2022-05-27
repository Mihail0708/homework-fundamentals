n = int(input())
special_number = False
for i in range(1, n+1):
    sum = 0
    digit = i
    if digit > 9:
        sum += digit // 10
        digit = i % 10

    if (sum + digit == 5) or (sum + digit == 7) or (sum + digit == 11):
        special_number = True
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')


n_strings = int(input())
for i in range(n_strings):
    string = input()
    if '.' not in string and ',' not in string and '_' not in string:
        print(f'{string} is pure.')
    else:
        print(f'{string} is not pure!')
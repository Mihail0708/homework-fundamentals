n_messages = int(input())
for i in range(n_messages):
    number = int(input())
    if number > 88:
        print('Bye.')
    else:
        if number == 86:
            print('How are you?')
        elif number == 88:
            print('Hello')
        else:
            print('GREAT!')
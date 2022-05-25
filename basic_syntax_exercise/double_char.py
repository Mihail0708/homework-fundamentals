command = input()
new_word = ''
while command != 'End':
    word = command
    if word == 'SoftUni':
        command = input()
        continue
    for letter in word:
        new_word += letter * 2
    print(new_word)
    new_word = ''
    command = input()

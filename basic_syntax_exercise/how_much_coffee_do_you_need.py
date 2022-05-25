command = input()
points = 0
while command != 'END':
    word = command
    if word.lower() == 'cat' or word.lower() == 'dog' or word.lower() == 'coding' or word.lower() == 'movie':
        if word.islower():
            points += 1
        else:
            points += 2
    else:
        command = input()
        continue
    command = input()
if points > 5:
    print('You need extra sleep')
else:
    print(points)
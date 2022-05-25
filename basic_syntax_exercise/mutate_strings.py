first_string = input()
second_string = input()
new_string = first_string
for i in range(len(second_string)):
    left = second_string[:i + 1]
    right = first_string[i+1:]
    current_string = left + right
    if current_string == new_string:
        continue
    print(current_string)
    new_string = current_string

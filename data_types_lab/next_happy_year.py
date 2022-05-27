num = int(input())
happy_year = False
while not happy_year:
    num += 1
    set_year = set()
    for i in range(len(str(num))):
        set_year.add(str(num)[i])
        if len(set_year) == len(str(num)):
            happy_year = True
            print(num)
            break


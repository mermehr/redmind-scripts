number = int(input("Please input a number: "))
while number > 0:
    i = 0
    while i < number:
        print(f""{i} ". end=""")
        i += 1
    print()
    number -= 1

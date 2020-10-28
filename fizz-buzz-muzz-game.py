print("Welcome to the fizz-buzz-muzz divisibility game! It's your math destination.")

choice = input("Do you want to start a game (y/n): ")
if choice.lower() != "y":
    print("End of the game")
else:
    num = input("Enter your number: ")
    num = int(num)

    for a in range(num, num+1):
        if a % 3 == 0 and a % 5 == 0 and a % 7 == 0:
            print("fizz-buzz-muzz")
        elif a % 3 == 0 and a % 5 == 0:
            print("fizz-buzz")
        elif a % 3 == 0 and a % 7 == 0:
            print("fizz-muzz")
        elif a % 5 == 0 and a % 7 == 0:
            print("buzz-muzz")
        elif a % 3 == 0:
            print("fizz")
        elif a % 5 == 0:
            print("buzz")
        elif a % 7 == 0:
            print("muzz")
        else:
            print(str(a) + " is not one of our numbers. Try another one.")

print("Easy currency converter: € to kn")

while True:
    Eu = int(input("Please enter the number of Euros: "))
    kn = Eu * 7.5835
    print("{0} Euros is/are {1} kunas.".format(Eu, kn))

    choice = input("Would you like another conversion? (y or n): ")

    if choice.lower() != "y":
        break

print("End of conversion. Thank your for using our converter.")

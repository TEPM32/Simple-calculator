print("Welcome to the TEPM PY Simple Calculator! \n"
      "Important note: % calculates a percentage of b. For exapmle, "
      "if a = 10 and b = 88, than a % b reveals what number is 10% of 88. In this case, it is 8.8.")

a = float(input("Please enter the first number: "))

oper = input("Select math operation (-. +. /, *, %, ^,): ")

b = float(input("Please enter the second number: "))

if oper == "+":
    print(a+b)
elif oper == "-":
    print(a-b)
elif oper == "/":
    print(a/b)
elif oper == "*":
    print(a*b)
elif oper == "^":
    print(a**b)
elif oper == "%":
    print(a/100*b)
else:
    print("Try with the proper operator.")

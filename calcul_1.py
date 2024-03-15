#from calcul_fun import add, sub, mul, div
while True:
    print("WELCOME TO MY CALCULATION")
    user = float(input("Enter a mathematical expression: "))
    if user == '+':
        result = sum(numbers)
    elif user == '-':
        result = lst[0] - sum(lst[1:])
    elif user == '*':
        result = 1
        for num in lst:
            result *= num
    elif user == '/':
        if 0 in lst[1:]:
            print("Error: Division by zero!")
            continue
        result = lst[0]
        for num in lst[1:]:
            result /= num
    else:
        print("Invalid operator.")
        continue

    print("Result:", result)
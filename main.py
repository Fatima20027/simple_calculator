while True:
    print("""select an operation:
                 1- ADD
                 2- MULTIPLY
                 3- SUBSTRACT
                 4- DIVISION
                 5- EXIT(to exit)
                  """)
    operator = input(">>>>: ")
    
    
    if operator == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("RESULT :", num1 + num2)
    
    elif operator == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("RESULT :", num1 * num2)
    elif operator == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1 - num2)
    elif operator == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1 / num2)
    elif operator == "5":
        break
        
    else:
        print("It's not valid, try again")

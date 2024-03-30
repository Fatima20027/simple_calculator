from funn import add, div, mul, sub

while True: 
    print("Please enter the operation you want")
    print("""    1- ADD
    2- MULTIPLY
    3- SUBSTRACT
    4- DIVISION
    5- EXIT(to exit)""")
    operation = input(">>>: ")
    if operation == "1":
        total = [int(x) for x in input("Enter Numbers You Want To Calculate here: ").split()]
        print("The Total Is:", add(total), end="\n")
    elif operation == "2":
        total = [int(x) for x in input("Enter Numbers You Want To Calculate here: ").split()]
        print("The Total Is:", mul(total), end="\n")
    elif operation == "3":
        total = [int(x) for x in input("Enter Numbers You Want To Calculate here: ").split()]
        print("The Total Is:", sub(total), end="\n")
    elif operation == "4":
        total = [int(x) for x in input("Enter Numbers You Want To Calculate here: ").split()]
        print("The Total Is:", div(total), end="\n")
    elif operation == "5":
        break
    else:
        print("It's not valid! please try again.", end="\n")



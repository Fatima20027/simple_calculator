def add(list):
    num = 0
    for i in range(len(list)):
        num = num + list[i]
    return num

def sub(list):
    num = 0
    for i in range(len(list)):
        num -= list[i]
    return num

def mul(list):
    num = 1
    for i in range(len(list)):
        num = num * list[i]
    return num

def div(list):
    num = 1
    for i in range(len(list)):
        if list[i] != 0:
            num = list[i] / num
        else:
            return "Error: Division by zero"
    return num
    
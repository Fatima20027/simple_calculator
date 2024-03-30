def add(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    return sum

def sub(list):
    sum = 0
    for i in range(len(list)):
        sum = sum - list[i]
    return sum

def mul(list):
    sum = 1
    for i in range(len(list)):
        sum = sum * list[i]
    return sum

def div(list):
    sum = 0
    for i in range(len(list)):
        if i != 0:
            sum = sum / list[i]
        else:
            return "Error: Division by zero"
    return sum
    
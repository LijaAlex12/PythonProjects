def add(num1, num2):
    sum = num1 + num2
    return sum


def multiply(num1, num2):
    pdt = num1 * num2
    return pdt

# higher order function: a function that takes as input another function
#the function that is input as parameter to the higher order function is called CALLBACK function


def calculator(num1, num2, operator):
    return operator(num1, num2)


print(calculator(1, 2, add))
print(calculator(3,4,multiply))
print('\n')

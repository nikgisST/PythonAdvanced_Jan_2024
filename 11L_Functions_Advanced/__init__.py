def calculator(operator):
    def addition(a, b):
        return a + b
    def subtraction(a, b):
        return a - b
    if operator == "+":
        return addition
    elif operator == "-":
        return subtraction

operation = calculator("+")
result = operation(2, 3)
print(result)                # 5



def greeting(name):
    hello = "Hello, "
    def say_hi():
        return hello + name
    return say_hi
print(greeting("Peter")())     # Hello, Peter
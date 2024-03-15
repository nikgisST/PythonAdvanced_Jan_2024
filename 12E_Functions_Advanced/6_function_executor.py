def sum():
    pass
sum.__name__        # функцията е обект и има клас както всики друг тип в пайтън

# def func_executor(*args):
#     return "\n".join(f"{fn.__name__} - {fn(*ar)}" for fn, ar in args)

def func_executor(*args):
    result = []

    for each_function, each_arguments in args:
        result.append(f"{each_function.__name__} - {each_function(*each_arguments)}")

    return "\n".join(result)


def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))



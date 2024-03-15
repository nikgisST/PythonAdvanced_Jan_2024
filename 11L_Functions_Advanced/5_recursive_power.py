def recursive_power(number, power):
    if power == 1:
        return number
    return number * recursive_power(number, power - 1)

print(recursive_power(2, 10))


def recursive_power(x, y):
    result = 1
    if y == 0:
        return result
    result = x * recursive_power(x, y - 1)
    return result

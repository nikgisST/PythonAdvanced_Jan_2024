def get_factorial(n: int):
    if n == 0:
        return 1

    result = n * get_factorial(n - 1)
    return result


n = int(input())
print(get_factorial(n))
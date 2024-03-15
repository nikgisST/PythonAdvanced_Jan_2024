number = [int(el) for el in input().split(", ")]
n = int(input())
for _ in range(n):
    index = int(input())

    try:
        print(number[index])
        print(10 / index)         #ZeroDivisionError: division by zero
    except IndexError:
        print("Invalid index")
    except ZeroDivisionError:
        print("Dev of zero is not possible")

print("This is the final row")



number = [1, 2, 3]
n = 1
counter = 0
for _ in range(n):
    index = 0

    try:
        print(number[index])
        b = {1: "one", 2: "two"}
        print(10 / index)
    except (IndexError, ZeroDivisionError):
        print("Invalid input")
    finally:
        counter += 1
        print(f"Counter is: {counter}")

print("This is the final row")



number = [1, 2, 3]
n = 1
counter = 0
for _ in range(n):
    index = 5

    try:
        print(number[index])
        b = {1: "one", 2: "two"}
        print(b[666])
        print(10 / index)
    except IndexError as ex:        # ex: list index out of range
        print(f"Invalid input error is: {str(ex)}")
    finally:
        counter += 1
        print(f"Counter is: {counter}")     # изпълнява се винаги
    #else:
     #   print("from else")           # изпълнява се само ако не влиза в EXCEPTIONS-ните



class ValueTooSmallError(Exception):
    """Raised when the input value is too small"""
    pass

amount_to_send = float(input())

if 0 <= amount_to_send < 1:
    raise ValueTooSmallError("Value is too low")

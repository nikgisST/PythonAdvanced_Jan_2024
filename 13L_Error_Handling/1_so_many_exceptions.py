numbers_list = [int(el) for el in input().split(", ")]    # error 2.1 --> ValueError: invalid literal for int() with base 10
# numbers_list = int(input().split(", "))       error 2.2 --> TypeError: int() argument must be a string,a bytes-like object or a number,not a 'list'
result = 1
for i in range(len(numbers_list)):     # error 3 --> TypeError: 'list' object cannot be interpreted as an integer
    number = numbers_list[i]         # error 4 --> IndexError: list index out of range
    if number <= 5:                # error 1 --> SyntaxError: invalid syntax
        result *= number
    elif 5 < number <= 10:
        result /= number
print(result)                # error 5 --> NameError: name 'total' is not defined

# 2, 5, 10	 -->  1.0

# numbers_list = int(input()).split(", ")
# result = 1
# for i in range(numbers_list):
#     number = numbers_list[i+1]
#     if number <= 5
#         result *= number
#     elif 5 < number <= 10:
#         result /= number
# print(total)
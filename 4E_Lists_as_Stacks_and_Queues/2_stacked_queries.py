numbers = []
count = int(input())

for each in range(count):
    type_of_digit = input().split()
    convert_to_int = [int(x) for x in type_of_digit]    #"1, 97" -> ["1", "97"] -> [1, 97]
    command = convert_to_int[0]

    if command == 1:
        # if len(convert_to_int) == 2:
        activity = convert_to_int[1]
        numbers.append(activity)
    elif command == 2:
        if numbers:
            numbers.pop()
    elif command == 3:
        if numbers:
            print(max(numbers))
    elif command == 4:
        if numbers:
            print(min(numbers))

numbers.reverse()
print(", ".join(map(str, numbers)))



numbers = []
count = int(input())

for each in range(count):
    type_of_digit = input().split()
    command = type_of_digit[0]

    if command == "1":
        activity = type_of_digit[1]
        numbers.append(activity)
    elif command == "2":
        if numbers:
            numbers.pop()
    elif command == "3":
        if numbers:
            print(max(numbers))
    elif command == "4":
        if numbers:
            print(min(numbers))

numbers.reverse()
print(*numbers, sep=", ")





numbers = []
count = int(input())

#def append(x: list):
    #numbers.append(x[1])

map_functions = {
    "1": lambda x: numbers.append(x[1]),
    "2": lambda x: numbers.pop() if numbers else None,
    "3": lambda x: print(max(numbers)) if numbers else None,
    "4": lambda x: print(min(numbers)) if numbers else None,
}

for each in range(count):
    type_of_digit = input().split()
    command = type_of_digit[0]
    map_functions[command](type_of_digit)

numbers.reverse()
print(*numbers, sep=", ")

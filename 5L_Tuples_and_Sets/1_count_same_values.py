numbers = tuple(map(float, input().split()))
nums_and_occurances = {}

for num in numbers:
    if num not in nums_and_occurances:
        nums_and_occurances[num] = 0
    nums_and_occurances[num] += 1

[print(f"{key} - {value} times") for key, value in
nums_and_occurances.items()]





numbers = tuple([float(el) for el in input().split()])
# numbers = tuple(float(el) for el in input().split())

same_values = {}

for current_number in numbers:
    if current_number not in same_values:
        same_values[current_number] = numbers.count(current_number)

for num, occurrence in same_values.items():
    print(f"{num} - {occurrence} times")




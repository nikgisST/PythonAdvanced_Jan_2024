import os.path

path = os.path.join("numbers.txt")

file = open(path)

total_amount = 0
for line in file.readlines():
    total_amount += int(line.strip())

print(total_amount)



numbers_file = open('numbers.txt', 'r')
numbers_sum = 0
for number in numbers_file:
    numbers_sum += int(number)
print(numbers_sum)

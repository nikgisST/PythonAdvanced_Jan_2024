numbers = list(map(int, input().split()))
target = int(input())

for i in range(len(numbers)):
    if numbers[i] == '':
        continue
    for j in range(i + 1, len(numbers)):
        if numbers[j] == '':
            continue
        if numbers[i] + numbers[j] == target:
            print(f"{numbers[i]} + {numbers[j]} = {target}")
            numbers[i] = ''
            numbers[j] = ''
            break



numbers = list(map(int, input().split()))
target = int(input())

targets = set()
hits_numbers = {}

for current_number in numbers:
    if current_number in targets:
        targets.remove(current_number)
        pair = hits_numbers[current_number]

        del hits_numbers[current_number]
        print(f'{pair} + {current_number} = {target}')

    else:
        searching_number = target - current_number
        targets.add(searching_number)
        hits_numbers[searching_number] = current_number



from collections import deque

water = int(input())
name = input()
people = deque()

while name != "Start":
    people.append(name)
    name = input()

command = input()

while command != "End":
    data = command.split()
    if len(data) == 1:
        liters_requested = int(data[0])
        person = people.popleft()
        if liters_requested <= water:
            water -= liters_requested
            print(f"{person} got water")
        else:
            print(f'{person} must wait')
    elif len(data) == 2:
        _, liters_to_add = data
        water += int(liters_to_add)

    command = input()
print(f"{water} liters left")






from collections import deque

water = int(input())
name = input()
people = deque()

while name != "Start":
    people.append(name)
    name = input()

command = input()

while command != "End":
    if "refill" in command:
        data = command.split()
        _, liters_to_add = data
        water += int(liters_to_add)
    else:
        liters = int(command)
        if liters <= water:
            water -= liters
            print(f"{people.popleft()} got water")
        else:
            print(f'{people.popleft()} must wait')
    command = input()
print(f"{water} liters left")

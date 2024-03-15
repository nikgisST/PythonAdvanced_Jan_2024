from collections import deque

# pump_data = []
# for _ in range(int(input())):
#     pump_data.append([int(x) for x in input().split()])

pump_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])  # [[1, 5], [10, 3], [1, 3], ....]

copied_pump = pump_data.copy()    # за да има нереферентни данни
gas_in_a_task = 0
index = 0

while copied_pump:
    petrol, distance = copied_pump.popleft()
    gas_in_a_task += petrol

    if gas_in_a_task >= distance:
        gas_in_a_task -= distance
    else:
        pump_data.rotate(-1)   # отляво надясно се премества първият елемент в списъка - отива последен
        copied_pump_data = pump_data.copy()   # за да има нереферентни данни
        index += 1
        gas_in_a_task = 0

print(index)


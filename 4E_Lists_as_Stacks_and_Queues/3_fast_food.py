from collections import deque

food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

for current_order in orders.copy():
    if food >= current_order:
        orders.popleft()
        food -= current_order
    else:
        print(f"Orders left:", *orders)   # " ".join([str(x) for x in orders])
        break
else:
    print("Orders complete")





from collections import deque

food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    current_order = orders.popleft()
    if food >= current_order:
        food -= current_order
    else:
        print(f"Orders left:", current_order, *orders)   # " ".join([str(x) for x in orders])
        break
else:
    print("Orders complete")

from collections import deque

cups = deque([int(cup) for cup in input().split()])   #deque([10, 20, 30, 40, 50])
bottles = deque([int(bottle) for bottle in input().split()])  #deque([20, 11])

wasted_water = 0

while cups and bottles:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()

    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
    else:
        cups.appendleft(current_cup - current_bottle)

if cups:
    print(f"Cups:", *cups)
elif not cups:
    print(f'Bottles:', *bottles)

print(f"Wasted litters of water: {wasted_water}")


seconds = 9                       #10
print(f"{seconds:02d}")   #09     #10

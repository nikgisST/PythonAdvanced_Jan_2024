from collections import deque

names = deque(input().split())
n_toss = int(input()) - 1

while len(names) > 1:
    names.rotate(- n_toss)
    removed_kid = names.popleft()
    print(f"Removed {removed_kid}")

last_kid = names.popleft()
print(f"Last is {last_kid}")
import time
from collections import deque

name = input()
customers = deque()

start_time = time.time()

while name != "End":
    if name == "Paid":
        while customers:
            print(customers.popleft())
    else:
        customers.append(name)
    name = input()

print(f"{len(customers)} people remaining.")
print("--- %s seconds ---" % (time.time() - start_time))


from collections import deque
customers = deque()
while True:
    name = input()
    if name == "Paid":
        while len(customers):
            print(customers.popleft())
    elif name == "End":
        print(f"{len(customers)} people remaining.")
        break
    else:
        customers.append(name)
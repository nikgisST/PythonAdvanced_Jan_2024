n = int(input())

names = set()
# names = []     с лист

for _ in range(n):
    name = input()
    names.add(name)
    # if name not in names:
        # names.append(name)    с лист

for every_name in names:
    print(every_name)
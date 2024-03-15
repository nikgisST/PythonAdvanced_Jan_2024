a = ["1", "2", "3"]
a = map(int, a)     # [int(el) for el in a] map работи само веднъж
for el in a:
    print(el, end=", ")       # 1, 2, 3
for el in a:
    print(el)
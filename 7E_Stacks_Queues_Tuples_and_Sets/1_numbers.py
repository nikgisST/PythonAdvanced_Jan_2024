first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

functions = {
    "Add First": lambda x: [first_set.add(int(el)) for el in x] ,   # first_set.update(second_set)
    "Add Second": lambda x: [second_set.add(int(el)) for el in x],
    "Remove First": lambda x: [first_set.discard(int(el)) for el in x],
    "Remove Second": lambda x: [second_set.discard(int(el)) for el in x],
    "Check Subset": lambda x: print(first_set.issubset(second_set) or first_set.issuperset(second_set)),
}

for _ in range(int(input())):
    first_command, second_command, *data = input().split()
    command = first_command + " " + second_command

    functions[command](data)

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")




# first_set = set(int(x) for x in input().split())
# second_set = set(int(x) for x in input().split())
#
# for _ in range(int(input())):
#     first_command, second_command, *data = input().split()
#
#     command = first_command + " " + second_command
#
#     if command == "Add First":
#         [first_set.add(int(el)) for el in data]
#     elif command == "Add Second":
#         [second_set.add(int(el)) for el in data]
#     elif command == "Remove First":
#         [first_set.discard(int(el)) for el in data]         # не хвърля грешка, ако еl не съществува
#     elif command == "Remove Second":
#         [second_set.discard(int(el)) for el in data]
#     elif command == "Check Subset":
#         print(first_set.issubset(second_set) or first_set.issuperset(second_set))
#         #print(first_set.issubset(second_set) or second_set.issuperset(first_set))
#
# print(*sorted(first_set), sep=", ")
# print(*sorted(second_set), sep=", ")
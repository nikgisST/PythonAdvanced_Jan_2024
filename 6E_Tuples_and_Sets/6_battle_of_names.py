odd_set = set()
even_set = set()
n = int(input())

for row in range(1, n + 1):
    names = input()
    ascii_sum_of_names = sum(ord(el) for el in names) // row

    if ascii_sum_of_names % 2 == 0:
        even_set.add(ascii_sum_of_names)
    else:
        odd_set.add(ascii_sum_of_names)

sum_odd_set, sum_even_set = sum(odd_set), sum(even_set)

if sum_odd_set == sum_even_set:
    print(*odd_set.union(even_set), sep=", ")
elif sum_even_set < sum_odd_set:
    print(*odd_set.difference(even_set), sep=", ")       # B - A
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")

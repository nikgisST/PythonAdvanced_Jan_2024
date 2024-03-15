longest_intersection = set()
n = int(input())

for _ in range(n):
    first_data, second_data = [el.split(",") for el in input().split("-")]    # "0,3-1,2" -> ["0,3-1,2"] -> [["0", "3"], ["1", "2"]]

    start_first_set = int(first_data[0])
    end_first_set = int(first_data[1])
    first_set = set(range(start_first_set, end_first_set + 1))    #{0, 1, 2, 3}

    start_second_set = int(second_data[0])
    end_second_set = int(second_data[1])
    second_set = set(range(start_second_set, end_second_set + 1))    #{1, 2}

    intersection = first_set.intersection(second_set)

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

result_formatting = (str(x) for x in longest_intersection)
max_len = len(longest_intersection)

print(f"Longest intersection is [{', '.join(result_formatting)}] with length {max_len}")




n = int(input())
longest_intersection = ''
max_len = 0

for _ in range(n):
    first_data, second_data = input().split('-')

    first_range = list(map(int, first_data.split(",")))
    second_range = list(map(int, second_data.split(",")))

    intersection_start = max(first_range[0], second_range[0])
    intersection_end = min(first_range[1], second_range[1])

    intersection = list(range(intersection_start, intersection_end + 1))

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection
        max_len = len(longest_intersection)

print(f"Longest intersection is {longest_intersection} with length {max_len}")


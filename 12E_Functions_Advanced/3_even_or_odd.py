# from typing import List
#
#
# def even_odd(*args: List[str, int]) -> List[int]:
def even_odd(*args):
    command = args[-1]
    #command = args.pop()

    if command == "even":
        return [num for num in args[:-1] if num % 2 == 0]
    else:
        nums = []
        for num in args[:-1]:
            if num % 2 != 0:
                nums.append(num)
        return nums
        # return [num for num in args[:-1] if num % != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))


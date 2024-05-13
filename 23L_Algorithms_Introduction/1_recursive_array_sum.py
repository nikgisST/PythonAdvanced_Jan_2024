def calc_sum(nums, idx=0):
    if idx == len(nums) - 1:
        return nums[idx]

    return nums[idx] + calc_sum(nums, idx + 1)
    # nums[2]== 3    +   1 br., 4        --> 3 + 4 = 7
    # nums[1]== 2    +   2 br., 3 and 4      --> 2 + 7 = 9
    # nums[0]== 1    +   3 br., 2 and 3 and 4    --> 1 + 9 = 10

nums = [int(x) for x in input().split()]
print(calc_sum(nums))




def calc_sum(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + calc_sum(nums[1:])


nums = list(map(int, input().split()))
print(calc_sum(nums))
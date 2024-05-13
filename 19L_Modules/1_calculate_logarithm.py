from math import log

number = int(input())
base = input()

if base == "natural":
    print(f"{log(number):.2f}")
else:
    print(f"{log(number, int(base)):.2f}")





from math import log

number = int(input())

try:
    base = int(input())
    print(f"{log(number, base):.2f}")
except ValueError:
    print(f"{log(number):.2f}")

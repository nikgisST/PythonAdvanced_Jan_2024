n = int(input())

usernames = set()

for _ in range(0, n):
    name = input()
    usernames.add(name)
print(*usernames, sep="\n")


print(*{input() for _ in range(int(input()))}, sep="\n")
from collections import deque

parentheses = deque(input())
open_parentheses = deque()

while parentheses:
    p = parentheses.popleft()
    if p in "{[(":
        open_parentheses.append(p)
    elif not open_parentheses:
        print("NO")
        break
    else:
        combination = open_parentheses.pop() + p
        if combination not in "(){}[]":
            print("NO")
            break
else:
    print("YES")




from collections import deque

parentheses = deque(input())
opening_brackets = "{[("
solutions = "{}[]()"
buffer = []
balanced = True
while parentheses:
    bracket = parentheses.popleft()
    if bracket in opening_brackets:
        buffer.append(bracket)
    else:
        if not buffer:
            balanced = False
            break
        br = buffer.pop()
        if br + bracket not in solutions:
            balanced = False
            break
print("YES") if balanced and not buffer else print("NO")
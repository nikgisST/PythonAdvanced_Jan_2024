text = input()
print((text[::-1]))


text = list(input())
while text:
    print(text.pop(), end="")


text = list(input())
stack = []
for i in range(len(text)):
    stack.append(text.pop())
print("".join(stack))


text = list(input())
stack = []
for i in range(len(text)):
    removed_element = text.pop()
    stack.append(removed_element)
print("".join(stack))


a = [10, 5, 3, 100]
result = a.remove(3)
print(result)            #резултат - NONE
print(a.remove(10))      #резултат - [10, 5, 3]


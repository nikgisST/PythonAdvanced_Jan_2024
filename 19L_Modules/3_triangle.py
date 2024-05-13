def print_triangle(size):
     for row in range(1, size + 2):
         print(*[col for col in range(1, row)])
     for row in range(size, 0, -1):
         print(*[col for col in range(1, row)])



#from PythonAdvanced_Jan_2024.19_Modules.main3 import print_triangle

n = int(input())
print_triangle(n)


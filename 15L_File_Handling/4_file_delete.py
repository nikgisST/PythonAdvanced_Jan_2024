import os

path = os.path.join("my_first_file.txt")
try:
    os.remove(path)
except FileNotFoundError:
    print("File already deleted!")



import os

path = os.path.join("my_first_file.txt")
if os.path.exists(path):
    os.remove(path)
else:
    print("File already deleted!")
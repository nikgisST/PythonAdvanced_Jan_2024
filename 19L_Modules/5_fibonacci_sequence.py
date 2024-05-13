#from PythonAdvanced_Jan_2024.19_Modules.main5 import create_sequence, locate_number

command = input()
sequence = []

while command != "Stop":
    if "Create" in command:
        _, _, number = command.split()
        number = int(number)
        sequence = create_sequence(number)
        print(*sequence)
    else:
        _, number = command.split()
        number = int(number)
        result = locate_number(number, sequence)
        print(result)

    command = input()
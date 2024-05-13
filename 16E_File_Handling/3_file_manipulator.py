import os

while True:
    command, *info = input().split("-")  # Replace-text.txt-a-b -> [text.txt, a, b]

    if command == "Create":
        file_name = info[0]
        with open(f"files\\{file_name}", "w"): pass

    elif command == "Add":
        file_name = info[0]
        content = info[1]
        with open(f"files\\{file_name}", "a") as file:
            file.write(f"{content}\n")

    elif command == "Replace":
        file_name = info[0]
        old_string = info[1]
        new_string = info[2]
        try:
            with open(f"files\\{file_name}", "r+") as file:
                text = file.read()
                text = text.replace(old_string, new_string)

                file.seek(0)
                file.write(text)
                file.truncate()

        except FileNotFoundError:
            print(f"An error occurred!")

    elif command == "Delet":
        file_name = info[0]
        try:
            os.remove(f"files\\{file_name}")
        except FileNotFoundError:
            print(f"An error occurred!")

    elif command == "End":
        break
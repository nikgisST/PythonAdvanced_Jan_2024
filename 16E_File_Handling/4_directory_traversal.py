import os


def save_extensions(dir_name, first_level=False):
    for filename in os.listdir(dir_name):                     #os.listdir(".")-търси в текущата директория,дава всички файлове в сегашната директория
        file = os.path.join(dir_name, filename)  # /03_file
        if os.path.isfile(file):  # os.path. - модул в модул
            extension = filename.split(".")[-1]
            # if extension not in extensions:    # for === in
            # extensions[extension] = []
            # extensions[extensiom].append(filename)
            extensions[extension] = extensions.get(extension, []) + [filename]
        elif os.path.isdir(file) and not first_level:
            save_extensions(file, first_level=True)

directory = input("Enter a directory: ")
extensions = {}  # [py: [python.py, hello.py], ...}
result = []

try:
    save_extensions(directory)
except FileNotFoundError:
    print("Directory not found!")

extensions = sorted(extensions.items(), key=lambda x: x[0])  # sorted връща list

# extension == key, files == values
for extension, files in extensions:  # extension => py, files => [one.py, two.py]...
    result.append(f".{extension}")

    for file in sorted(files):
        result.append(f"- - - {file}")

with open("files/report.txt", "w") as report_file:
    report_file.write('\n'.join(result))
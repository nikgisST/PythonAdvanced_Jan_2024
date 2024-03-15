numbers_dictionary = {}        # {one: 1}
line = input()        # one

while line != "Search":
    number_as_string = line    # one
    try:
        number = int(input())    # 1
        numbers_dictionary[number_as_string] = number
    except ValueError:             # error 2.0
        print(f"The variable number must be an integer")
    line = input()                 # error 1.1

line = input()
while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:               # error 3.1
        print(f"Number does not exist in dictionary")
    line = input()                 # error 1.2

line = input()
while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:               # error 3.2
        print(f"Number does not exist in dictionary")
    line = input()                 # error 1.3

print(numbers_dictionary)


# one
# 1
# two
# 2
# Search
# one
# Remove
# two
# End     --> 1
#            {'one': 1}

# one
# two
# Search
# Remove
# End    --> The variable number must be an integer
#            {}


# one
# 1
# Search
# one
# Remove
# two
# End    -->  1
#             Number does not exist in dictionary
#            {'one': 1}





# numbers_dictionary = {}
#
# line = input()
#
# while line != "Search":
#     number_as_string = line
#     number = int(input())
#     numbers_dictionary[number_as_string] = number
#
# line = input()
#
# while line != "Remove":
#     searched = line
#     print(numbers_dictionary[searched])
#
# line = input()
#
# while line != "End":
#     searched = line
#     del numbers_dictionary[searched]
#
# print(numbers_dictionary)


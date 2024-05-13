symbols = ("-", ",", ".", "!", "?")

with open("files\\text.txt", "r") as even_lines_file:
    text = even_lines_file.readlines()

for row in range(0, len(text), 2):

    for symbol in symbols:
        text[row] = text[row].replace(symbol, "@")      # text == list  row == index

    split_each_word = text[row].split()
    reverse_order_of_words = split_each_word[::-1]
    print(*reverse_order_of_words)

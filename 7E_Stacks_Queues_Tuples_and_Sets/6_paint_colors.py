from collections import deque

words = deque(input().split())    # d yel blu e low redd

colors = {"red", "yellow", "blue", "purple", "orange", "green"}
requested_colors = {
    "orange": {"red", "yellow"},
    "purple": {"blue", "red"},
    "green": {"yellow", "blue"},
}

mine = []

while words:
    first_word = words.popleft()
    second_word = words.pop() if words else ''
    mix_1 = first_word + second_word
    mix_2 = second_word + first_word

    for color in (mix_1, mix_2):
        if color in colors:
            mine.append(color)
            break
    else:
        remove_last_char_of_first_word = first_word[:-1]
        remove_last_char_of_second_word = second_word[:-1]
        for el in (remove_last_char_of_first_word, remove_last_char_of_second_word):   # 'd' 'red' -> '', 'red'
            if el:
                middle_of_origin_words_string = len(words) // 2
                words.insert(middle_of_origin_words_string, el)

for color in set(requested_colors.keys()).intersection(mine):
    # requested_colors.keys() -> {orange, green, purple}.intersection(["orange", "red", "yellow"])
    if not requested_colors[color].issubset(mine):
        # {"orange"}, mine = {"blue", "red"}
        mine.remove(color)
print(mine)


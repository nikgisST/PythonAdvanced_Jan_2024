occurences = {}

for symbol in input():
    occurences[symbol] = occurences.get(symbol, 0) + 1

for symbol, times in sorted(occurences.items()):    # (("a", 1), ("b", 3))
    print(f"{symbol}: {times} time/s")




text = input()
for symbol in sorted(set(text)):
    counter = text.count(symbol)
    print(f"{symbol}: {counter} time/s")
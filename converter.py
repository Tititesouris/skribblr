data = open("input/input.txt").read().split(",")
print(data)

last_word = data[0]
for word in data:
    smallest_length = min(len(last_word), len(word))
    same_letters = 0
    for i in range(smallest_length):
        if last_word[i] == word[i]:
            same_letters += 1
        else:
            break
    if same_letters / smallest_length > 0.95:
        print(last_word, word)
    last_word = word

with open("output/output.txt", "w") as f:
    f.write(",".join(data))
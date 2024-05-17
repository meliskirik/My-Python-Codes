word = "life is beautiful"
def letter_frequency(word):
    frequency = dict()
    list_of_letters = list(word)
    for letter in list_of_letters:

        if letter not in frequency:
            frequency[letter] = 1
        else:
            frequency[letter] += 1

    print(frequency)



letter_frequency(word)

''' letter = "python.rocks"
d = dict()
for c in letter:
    if c not in d:
        d[c] = 1

    else:
        d[c] = d[c] + 1

print(d) '''
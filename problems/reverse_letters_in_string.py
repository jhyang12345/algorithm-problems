def reverse_letters(sentence):
    words = sentence.split()
    words = ["".join(list(word)[::-1]) for word in words]
    return " ".join(words)

print(reverse_letters("The cat in the hat"))
# ehT tac ni eht tah

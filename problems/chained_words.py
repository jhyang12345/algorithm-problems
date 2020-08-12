# Two words can be 'chained' if the last character of the first word is the same as the first character of the second word.
#
# Given a list of words, determine if there is a way to 'chain' all the words in a circle.
#
# Example:
# Input: ['eggs', 'karat', 'apple', 'snack', 'tuna']
# Output: True
# Explanation:
# The words in the order of ['apple', 'eggs', 'snack', 'karat', 'tuna'] creates a circle of chained words.

from collections import defaultdict

def chainedWords(words):
    n = len(words)
    tails = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i != j:
                cur = words[i]
                tail = words[j]
                if cur[-1] == tail[0]:
                    tails[cur].append(tail)
    used = {word: False for word in words}
    start = words[0]
    used[start] = True
    count = 1
    cur = start
    print(tails)
    while count < n:
        selected = None
        for word in tails[cur]:
            if not used[word]:
                selected = word
                break
        if not selected:
            return False
        count += 1
        cur = selected

    return cur[-1] == start[0]

print(chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna']))
print(chainedWords(['apple', 'eggs']))
print(chainedWords(['apple', 'eggs', 'salsa']))

S = "abppplee"
D = ["able", "ale", "apple", "bale", "kangaroo"]

def find_longest_substring(S, D):
    longest_word = ""
    l = 0
    for word in D:
        i = 0
        j = 0
        while j < len(word) and i < len(S):
            ch_S = S[i]
            ch_word = word[j]
            if ch_S == ch_word:
                i += 1
                j += 1
            else:
                i += 1
        if j == len(word):
            longest_word = word
            l = len(word)
    return longest_word

print(find_longest_substring(S, D))
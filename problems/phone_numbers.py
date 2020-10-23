# Given a phone number, return all valid words that can be created using that phone number.
#
# For instance, given the phone number 364
# we can construct the words ['dog', 'fog'].
#
# Here's a starting point:

lettersMaps = {
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
    0: []
}

validWords = ['dog', 'fish', 'cat', 'fog']

def makeWords(phone):
    letter_to_number = {}
    for key in lettersMaps:
        for letter in lettersMaps[key]:
            letter_to_number[letter] = key
    ret = []
    for word in validWords:
        if len(word) != len(phone):
            continue
        flag = True
        for i, letter in enumerate(word):
            if str(letter_to_number[letter]) == str(phone[i]):
                continue
            else:
                flag = False
                break
        if flag:
            ret.append(word)
    return ret

print(makeWords('364'))
# ['dog', 'fog']

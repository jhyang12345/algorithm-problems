import sys

def longest_palindrome(text):
    max_len = 0
    palindrome = ''
    for i in range(len(text)):
        cur_len = 1
        start = i
        end = i
        while start >= 1 and end < len(text) - 1:
            start -= 1
            end += 1
            if text[start] == text[end]:
                cur_len += 2
            else:
                break
        if cur_len > max_len:
            palindrome = text[start + 1: end]
        max_len = max(cur_len, max_len)

        if i + 1 < len(text):
            start = i
            end = i + 1
            if text[start] == text[end]:
                cur_len = 2
                while start >= 1 and end < len(text) - 1:
                    start -= 1
                    end += 1
                    if text[start] == text[end]:
                        cur_len += 2
                    else:
                        break
                if cur_len > max_len:
                    palindrome = text[start + 1: end]
                max_len = max(cur_len, max_len)
    print(text)
    print(palindrome)
    return max_len

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print(n)
    for _ in range(n):
        text = sys.stdin.readline().strip()
        print(longest_palindrome(text))

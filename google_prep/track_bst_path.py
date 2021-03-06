def bst_path(number):
    ret = []
    num = number
    while num > 1:
        r = num % 2
        if r == 1:
            ret.append('right')
        else:
            ret.append('left')
        num //= 2
    return ret[::-1]



#          1
#    2           3
#  4    5     6     7
# 8 9 10 11 12 13 14 15

print(bst_path(15))
print(bst_path(11))
print(bst_path(10))

# You are the manager of a number of employees who all sit in a row.
# The CEO would like to give bonuses to all of your employees, but since the
# company did not perform so well this year the CEO would like to keep the bonuses to a minimum.
#
# The rules of giving bonuses is that:
# - Each employee begins with a bonus factor of 1x.
# - For each employee, if they perform better than the person sitting next to them,
# the employee is given +1 higher bonus (and up to +2 if they perform better than both people to their sides).
#
# Given a list of employee's performance, find the bonuses each employee should get.

def getBonuses(performance):
    n = len(performance)
    cache = [1 for _ in range(n)]
    for i in range(1, n):
        if performance[i] > performance[i -1]:
            cache[i] += 1
    for i in range(n - 2, -1, -1):
        if performance[i] > performance[i + 1]:
            cache[i] += 1
    return(cache)

print(getBonuses([1, 2, 3, 2, 3, 5, 1]))
# [1, 2, 3, 1, 2, 3, 1]

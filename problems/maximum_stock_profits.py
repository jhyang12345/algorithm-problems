# Maximum Profit From Stocks

def max_profits(stocks):
    min_til_now = [-1 for _ in range(len(stocks))]
    min_til_now[0] = stocks[0]
    for i in range(1, len(stocks)):
        min_til_now[i] = min(min_til_now[i - 1], stocks[i])
    # print(min_til_now)
    max_profit = 0
    for i in range(len(stocks)):
        max_profit = max(max_profit, stocks[i] - min_til_now[i])
    print(max_profit)



arr = [9, 11, 8, 5, 7, 10]
max_profits(arr)

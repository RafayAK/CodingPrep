'''
This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a
company in chronological order, write a function that calculates the
maximum profit you could have made from buying and selling that stock once.
You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5,
since you could buy the stock at 5 dollars and sell it at 10 dollars.

'''

def find_max_profit(stocks):

    if not stocks:
        return float("-inf")

    max_profit = float("-inf")

    for s in stocks[1:]:
        # calculate the first profit
        if max_profit is None:
            max_profit = s - stocks[0]

        if max_profit < s - stocks[0]:
            max_profit = s - stocks[0]

    return max(max_profit, find_max_profit(stocks[1:]))

if __name__ == '__main__':
    stocks = [9, 11, 8, 5, 7, 10]
    print(find_max_profit(stocks))
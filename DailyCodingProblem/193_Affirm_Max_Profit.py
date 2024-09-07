"""
This problem was asked by Affirm.

Given an array of numbers representing the stock prices of a company in chronological order,
write a function that calculates the maximum profit you could have made from buying and selling that stock.
You're also given a number fee that represents a transaction fee for each buy and sell transaction.

You must buy before you can sell the stock, but you can make as many transactions as you like.

For example, given [1, 3, 2, 8, 4, 10] and fee = 2, you should return 9,
since you could buy the stock at 1 dollar, and sell at 8 dollars, and then buy
it at 4 dollars and sell it at 10 dollars. Since we did two transactions,
there is a 4 dollar fee, so we have 7 + 6 = 13 profit minus 4 dollars of fees.

"""

"""
Max profit can be solved greedily.
We can either Hold stock hoping to make profit at a later time or Not-hold. 

So we'll maintain 2 states:
    - total profit while a stock is held, let's call this state var "hold"
    - total profit while no-stock is held, let's call this state var "not_hold" 
    
we update both as follows:
    - if not_hold - price (i.e we buy a stock) > curr hold value -> lets buy this stock at price "p"
      so then our new holding profit is not_hold - p => hold = max(hold, not_hold - p)
    - if hold + price - fee (i.e we make the transaction and convert all assets paying a fee) > current 
      not_holding profit so then our new total profit while not holding any stock is hold + price - fee
       giving us => not_hold = max(not_hold, hold + price - fee)
       
We return not_hold.

"""


def max_profit_with_fee(stock_prices, fee):
    if not stock_prices:
        return 0

    hold = -stock_prices[0]  # initial holding profit is negative as when we get the first stock we are spending
    not_hold = 0  # if hadn't bought the first stock out profit would be 0
    last_bought = stock_prices[0]
    transactions = []

    for price in stock_prices[1:]:
        if not_hold - price > hold:
            last_bought = price
        hold = max(hold, not_hold - price)

        if hold + price - fee > not_hold:
            transactions.append((last_bought, price))
        not_hold = max(not_hold, hold + price - fee)
    print(f"Total of {len(transactions)} transactions performed")
    for buy, sell in transactions:
        print(f"Bought at {buy} and sold at {sell}")
    return not_hold


if __name__ == '__main__':
    assert max_profit_with_fee([1, 3, 2, 8, 4, 10], 0) == 14
    print("----------------------")
    assert max_profit_with_fee([1, 3, 2, 8, 4, 10], 2) == 9

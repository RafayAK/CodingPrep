"""
This problem was asked by Facebook.

Given an array of numbers representing the stock prices of a company in chronological order and an integer k,
return the maximum profit you can make from k buys and sells.
You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.
"""


def max_profit(prices, k):
    def helper(p, curr_share=None, profit=0, buys=0, sells=0):
        if len(p) == 0 or (buys == k and sells == k):
            return profit

        result = []

        if curr_share is None:
            # can't sell share
            # so buy or ignore

            if buys < k:
                result.append(helper(p=p[1:], curr_share=p[0], profit=profit-p[0], buys=buys+1, sells=sells))

            result.append(helper(p=p[1:], curr_share=curr_share, profit=profit, buys=buys, sells=sells))
        else:
            # sell, or ignore
            if sells < k:
                result.append(helper(p=p[1:], curr_share=None, profit=profit+p[0], buys=buys, sells=sells+1))

            result.append(helper(p=p[1:], curr_share=curr_share, profit=profit, buys=buys, sells=sells))

        return max(result)

    return helper(prices)


if __name__=="__main__":
    print(max_profit([5,2,4], k=1))
    print(max_profit([5, 2, 4, 0,1], k=2))
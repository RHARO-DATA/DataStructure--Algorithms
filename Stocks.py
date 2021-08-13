"""
Sell stock
input [7,1,5,3,6,4]
output[5]

""""
def max_profit(prices):

    if prices ==[]:
        return 0
    res = 0
    min = prices [0]
    for p in prices:
        if min > p:
            min = p
        res = max(res,p-min)s
    return res

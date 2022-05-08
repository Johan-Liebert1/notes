"""  
Given an array A of stock prices and number of allowed transactions k, 
find the maximum profit that can be made by buying or selling a stock for k transactions.
Buying and then selling = 1 transaction

have to sell before buying another stock. 
"""

_ = """

create a table with rows as prices and columns as transactions

prices = [5, 11, 3, 50, 60, 90]
transactions = 2

answer = 93


    5,      11,     3,      50,     60,     90
0   0        0      0        0       0       0

1   0        6      6       47      57      87

2   0

0s on at transactions 0 means that we neither bought, nor sold so 0 profit, and 0 in the first column means
that we sold whatever we bought the same day so no profit

d = day (price)
t = transaction

f = max (
    profit[t][d - 1],

    prices[d] +  max( [ -prices[x] + profit[t - 1][d]  for x in range(0, d) ] ) 
)

max( [ -prices[x] + profit[t - 1][x]  for x in range(0, d) ] )

let's say we want to calculate at 60 for the 2nd transaction. 

-prices[x] = we buy the stock at x, so we're prices[x] down
+profit[t - 1][x] = since on the second transaction we bought at x, in the previous transaction we must sell at or 
before x, but since we'll be putting max profit anyway even if we sold before x, x will have the highest profit

Example calculating profit at 60 on 2nd transaction, buy 50 so down by 50, but got 47 by selling 50

"""

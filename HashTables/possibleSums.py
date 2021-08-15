'''
You have a collection of coins, and you know the values of the coins and the quantity of each type of coin in it. You want to know how many distinct sums you can make from non-empty groupings of these coins.

Example

For coins = [10, 50, 100] and quantity = [1, 2, 1], the output should be
possibleSums(coins, quantity) = 9.

Here are all the possible sums:

50 = 50;
10 + 50 = 60;
50 + 100 = 150;
10 + 50 + 100 = 160;
50 + 50 = 100;
10 + 50 + 50 = 110;
50 + 50 + 100 = 200;
10 + 50 + 50 + 100 = 210;
10 = 10;
100 = 100;
10 + 100 = 110.
As you can see, there are 9 distinct sums that can be created from non-empty groupings of your coins.'''

# lst = [10, 50, 50, 100]

# nC0 + nC1 + nC2 + nC3 + ... + nCn = 2^n

def factorial(n):
    if n < 2:
        return 1

    else:
        return n * factorial(n - 1)



def possibleSums(coins, quantity):
    total = 0
    divideBy = []

    for i in quantity:
        if i > 1:
            divideBy.append(i)
        total += i

    print(total)

    final_sol = 2 ** total - 2

    print(divideBy)

    prod_fact = 1

    for i in divideBy:
        prod_fact *= factorial(i)

    return (final_sol // prod_fact) + (total - 2) 


print(possibleSums(coins = [10, 50, 100], quantity = [1, 2, 1]))


    

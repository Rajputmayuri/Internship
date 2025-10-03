"""Brute Force Solution"""

prices = [7, 2, 1, 5, 6, 4, 8]
max_profit = 0
n = len(prices)
for i in range(0, n):
    for j in range(i + 1, n):
        if prices[j] > prices[i]:
            p = prices[j] - prices[i]
            max_profit = max(p, max_profit)
print(max_profit)

"""Time Complexity = O(N(N+1)/2) = O(N^2)
    Space Complexity = O(1)"""

"""Optimal Solution"""

prices = [7, 2, 1, 5, 6, 4, 8]
max_profit = 0
min_price = float("inf")
n = len(prices)
for i in range(0, n):
    min_price = min(min_price, prices[i])
    max_profit = max(max_profit, prices[i] - min_price)
print(max_profit)

"""Time Complexity : O(N)
    Space Complexity : O(1)"""

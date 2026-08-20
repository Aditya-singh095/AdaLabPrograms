from typing import List


# -------------------------
# 2D Dynamic Programming
# -------------------------
def knapsack_01_2d(
    weights: List[int],
    values: List[int],
    capacity: int
) -> int:

    n = len(weights)

    # dp[i][w] = maximum value using first i items
    # with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = weights[i - 1]
        value = values[i - 1]

        for w in range(capacity + 1):

            # Don't take the item
            dp[i][w] = dp[i - 1][w]

            # Take the item if it fits
            if weight <= w:
                dp[i][w] = max(
                    dp[i][w],
                    value + dp[i - 1][w - weight]
                )

    return dp[n][capacity]


# -------------------------
# 1D Dynamic Programming
# -------------------------
def knapsack_01(
    weights: List[int],
    values: List[int],
    capacity: int
) -> int:

    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        weight = weights[i]
        value = values[i]

        # Traverse backwards so each item is used only once
        for w in range(capacity, weight - 1, -1):
            dp[w] = max(
                dp[w],
                value + dp[w - weight]
            )

    return dp[capacity]


# -------------------------
# Example
# -------------------------

weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

print("2D DP:", knapsack_01_2d(weights, values, capacity))
print("1D DP:", knapsack_01(weights, values, capacity))

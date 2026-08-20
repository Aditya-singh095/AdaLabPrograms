from typing import List


def floyd_warshall(graph: List[List[int]]) -> List[List[int]]:
    n = len(graph)

    # Make a copy so the original graph is not modified
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )

    return dist


def optimal_bst(keys: List[int], freq: List[int]) -> int:
    n = len(keys)

    if n == 0:
        return 0

    # dp[i][j] = minimum cost for keys i through j
    dp = [[0] * n for _ in range(n)]

    # Prefix sum for frequencies
    prefix = [0] * (n + 1)

    for i in range(n):
        prefix[i + 1] = prefix[i] + freq[i]

    def total_freq(i, j):
        return prefix[j + 1] - prefix[i]

    # One-key trees
    for i in range(n):
        dp[i][i] = freq[i]

    # Consider increasing lengths
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            dp[i][j] = float('inf')

            # Try every key as root
            for root in range(i, j + 1):

                left = dp[i][root - 1] if root > i else 0
                right = dp[root + 1][j] if root < j else 0

                cost = left + right + total_freq(i, j)

                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]


# -------------------------
# Floyd-Warshall Example
# -------------------------

INF = float('inf')

graph = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]

result = floyd_warshall(graph)

print("Shortest path matrix:")
for row in result:
    print(row)


# -------------------------
# Optimal BST Example
# -------------------------

keys = [10, 12, 20]
freq = [34, 8, 50]

print("\nOptimal BST cost:", optimal_bst(keys, freq))

from typing import List


class TSPSolver:

    def solve_tsp(self, dist_matrix: List[List[int]]) -> int:
        n = len(dist_matrix)

        if n == 0:
            return 0

        # dp[mask][i] = minimum cost to visit all cities
        # in mask and end at city i
        dp = [[float('inf')] * n for _ in range(1 << n)]

        # Start from city 0
        dp[1][0] = 0

        for mask in range(1 << n):
            for current in range(n):

                if dp[mask][current] == float('inf'):
                    continue

                # Try visiting every unvisited city
                for next_city in range(n):

                    if mask & (1 << next_city):
                        continue

                    new_mask = mask | (1 << next_city)

                    new_cost = (
                        dp[mask][current]
                        + dist_matrix[current][next_city]
                    )

                    dp[new_mask][next_city] = min(
                        dp[new_mask][next_city],
                        new_cost
                    )

        # All cities visited
        full_mask = (1 << n) - 1

        # Return to starting city
        answer = float('inf')

        for city in range(1, n):
            answer = min(
                answer,
                dp[full_mask][city] + dist_matrix[city][0]
            )

        return answer


# -------------------------
# Example
# -------------------------

dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

solver = TSPSolver()

print("Minimum tour cost:",
      solver.solve_tsp(dist_matrix))

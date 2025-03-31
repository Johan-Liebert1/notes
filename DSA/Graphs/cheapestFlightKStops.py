from typing import List

"""  
basically traversing every path and just returning the min cost one
"""


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:

        visited = set()
        graph = {}
        final_cost = float("inf")

        for f, t, c in flights:
            if f in graph:
                graph[f].append((t, c))
            else:
                graph[f] = [(t, c)]

        def dfs(node, stop, total_cost):
            nonlocal final_cost

            if stop > k:
                return

            if node == dst:
                final_cost = min(final_cost, total_cost)
                return

            if node not in graph:
                return

            visited.add(node)

            for to, cost in graph[node]:
                if to not in visited:
                    dfs(to, stop + 1, total_cost + cost)

            visited.remove(node)

        dfs(src, -1, 0)

        return final_cost if final_cost != float("inf") else -1


print(
    Solution().findCheapestPrice(
        n=4,
        flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
        src=0,
        dst=3,
        k=1,
    )
)

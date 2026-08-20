from collections import deque
from typing import List, Set


class Solution:
    """
    Intuition:
        This problem is essentially asking us to find the number of connected components
        in a graph. We keep track of the remaining "available" cities to explore in a set.
        As we traverse the graph, we remove each city we process from the pool of available
        cities and only initiate DFS from cities that have not yet been explored. This way,
        if cities are connected with each other, they are treated as a single province.

    Runtime:
        O(V + E) where V is the number of nodes i.e. cities and E is the number of edges i.e.
        connections between cities.

    Memory: O(V) where V is the number of nodes/vertices i.e. cities.
    """

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Helper function
        def dfs(city: int, availableCities: Set[int]):
            q = deque([city])
            availableCities.remove(city)

            while q:
                c = q.pop()

                for i in range(N):
                    if isConnected[c][i] == 1 and i in availableCities:
                        q.append(i)
                        availableCities.remove(i)

        N = len(isConnected)
        availableCities = set(range(N))
        numProvinces = 0

        for city in range(N):
            if city in availableCities:
                dfs(city, availableCities)
                numProvinces += 1

        return numProvinces

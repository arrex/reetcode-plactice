from collections import defaultdict, deque
from typing import List


class Solution:
    """
    Intuition:
        This problem can be modeled as a weighted graph, but requires some math. The key observation
        is the relationship between equations.

        For example:
            Let's say we have equations A / B = 2.0 and B / C = 3.0

            From this we can infer that A = 2.0 * B and C = B / 3.0

            Thus, if we are asked to infer A / C, we have that

            A / C = (2.0 * B) / (B / 3.0) = (2.0 * B) * (3.0 / B) = 6.0 = (A / B) * (B / C)

            Conversely, if we are asked the opposite/reverse, we have that

            C / A = (B / 3.0) / (2.0 * B) = B / (6.0 * B) = 1 / 6.0 =  1 / [(A / C) * (B / C)]

        From these relationships, we notice that taking a forward edge (i.e. an original equation
        with a value) that is given to us, we perform a multiplication. If we take a backwards edge,
        we need to take the original value 'w' and compute the complement '1 / w'.

        Thus, we start out algorithm by building an adjacency list that encodes all the weighted
        forward edges. We explicitly add backwards edges with reciprocal weights too.

        Then, for each query, we traverse the graph to compute the resulting value. The accumulated
        result represents the ongoing value of the compound division. If DFS does not lead us to our
        target node, we know that there is no way for us to infer the given equation and so we return
        -1.0. Similarly, if either variable in the given query does not exist in the graph, we cannot
        determine its value.

    Runtime:
        O(N) to build the adjacency list where N is the number of equations given to us

        O(V + E) for each DFS where V is the number of variables and E is the number of
        edges or equations since equations represent relationships between variables here.

        Overall, we need O(N * (V + E)) to build our 'ans' array where N is the number of
        queries (on the same scale as equations input).

    Memory:
        O(V + E) for the adjancency list. Each node is stored once i.e. O(V) and each equation representing
        an edge is stored twice i.e. O(2E).

        'ans' array is on the scale of the 'queries' input which itself is on the same scale as 'equations'.
        Thus, the memory complexity of the 'ans' array is O(N) where N ~ E.

        Overall, the memory complexity is bounded by O(V + E).
    """

    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        # Step 1. Build adjacency list
        adj = defaultdict(list)

        for (u, v), w in zip(equations, values):
            # Original edge
            adj[u].append((v, w))
            # Reverse edge
            adj[v].append((u, 1 / w))

        # Step 2. For each query, traverse the graph and compute the final result
        ans = []

        # Helper DFS function
        def dfs(src, target):
            # Encode as (node, result)
            q = deque([(src, 1.0)])
            seen = {src}

            while q:
                node, res = q.pop()

                if node == target:
                    return res

                for nei, weight in adj[node]:
                    if nei not in seen:
                        q.append((nei, res * weight))
                        seen.add(nei)

            # If no valid path was found, that means there is no possible way
            # to infer value of the query, so return -1.0
            return -1.0

        for u, w in queries:
            if u not in adj or w not in adj:
                ans.append(-1.0)
            else:
                ans.append(dfs(u, w))

        return ans

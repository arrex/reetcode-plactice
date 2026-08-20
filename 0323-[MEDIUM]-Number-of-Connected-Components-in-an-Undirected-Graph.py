from collections import deque
from typing import List


class Solution:
    """
    Intuition:
        The solution can be divided into 2 main steps.

        Firstly, we need to compute the adjacency list of the graph.

        Then, we keep track of the nodes we have seen and use BFS to
        remove all the nodes reachable from that source node. Repeat
        this step until we have seen all nodes.

    Runtime:
        O(n^2) to build the adjancency list. O(n) to compute the number
        of connected components since each node is processed once. Overall
        runtime is bounded by O(n^2).

    Memory:
        O(n^2) for the adjacency list. O(n) for the deque. Bounded by O(n^2).
    """

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adj list
        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        seen = set()

        def bfs(src):
            q = deque([src])

            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    seen.add(node)

                    for nei in adj[node]:
                        if nei not in seen:
                            q.append(nei)

        res = 0

        for i in range(n):
            if i not in seen:
                bfs(i)
                res += 1

        return res

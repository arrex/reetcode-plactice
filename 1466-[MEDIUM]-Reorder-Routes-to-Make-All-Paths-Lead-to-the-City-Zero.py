from collections import deque
from typing import List


class Solution1:
    """
    Intuition:
        The key thing to notice is that the graph forms a network tree rooted at
        city 0. As such, our goal is to traverse the entire tree.

        The constraint, though, is that we are given a directed graph. To deal
        with this fact, we can introduct reverse edges to model each connection
        as bidirectional. To keep track of original edges, we will assign an
        extra bit. A value of 1 indicates the edge is in the original connections
        and a value of 0 indicates the edge is "artificially" introduced.

        We then traverse the tree using DFS and keep track of where we came from
        i.e. the parent. If the edge going from the parent (which radiates from
        city 0) to the current city is in the original connections, we know we
        have to flip its direction to make it point towards the root of city 0.

    Runtime:
        O(V + E) ~ O(V) where V is the number of cities
        V ~= E since we have a network tree i.e. n nodes and n - 1 edges.

    Memory:
        O(V) where V is the number of cities

    Notes:
        Intuition is absolutely correct, but runtime on Leetcode is a bit lackluster.
        We can rewrite some parts of the logic to optimize it.
    """

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = {i: set() for i in range(n)}

        for u, v in connections:
            # 1 = original edge
            adj[u].add((v, 1))
            # 0 = artificial reverse edge
            adj[v].add((u, 0))

        # Number of edges that need to be flipped
        res = 0
        # DFS from city 0, encode as (city, parent)
        q = deque([0])
        seen = {0}

        while q:
            city = q.pop()

            for nei, dir in adj[city]:
                if nei not in seen:
                    # Taking an original edge that needs to be flipped
                    if dir == 1:
                        res += 1

                    q.append(nei)
                    seen.add(nei)

        return res


class Solution2:
    """
    Intuition:
        Same as Solution1. However, we use more basic data structures to reduce overhead.
        We also separate the original and reverse edges into 2 different adjacency lists
        to avoid the need for an extra 1/0 bit abstraction.
    """

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        revAdj = [[] for _ in range(n)]

        for u, v in connections:
            # Original edges
            adj[u].append(v)
            # Artificial reverse edges
            revAdj[v].append(u)

        # Number of edges that need to be flipped
        res = 0
        # DFS from city 0, encode as (city, parent)
        q = deque([0])
        seen = [False] * n
        seen[0] = True

        while q:
            city = q.pop()

            # Any edge we take to reach further cities from the source of city 0
            # that exist in the original connections needs to be flipped
            for nei in adj[city]:
                if not seen[nei]:
                    res += 1
                    q.append(nei)
                    seen[nei] = True

            for nei in revAdj[city]:
                if not seen[nei]:
                    q.append(nei)
                    seen[nei] = True

        return res

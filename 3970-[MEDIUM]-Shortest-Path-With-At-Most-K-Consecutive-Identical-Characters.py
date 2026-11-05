import heapq
from typing import List


class Solution:
    """
    Intuition:
        Use Dijkstra's. Keep track of seen states for efficiency.

    Runtime:
        We have v nodes and e edges.

        Building the adjacency list takes O(v + e).

        We can push up to O(ek) entries into the heap, meaning that
        pushing and popping costs O(log(ek)). Given that we have O(ek)
        possible states to explore, this gives our graph traversal
        loop a runtime of O(ek * log(ek)).

        Thus, the overall runtime is O(v + e + ek * log(ek)).

    Memory:
        The adjacency list takes O(v + e) space.

        The priority queue has up to O(ek) entries, so O(ek) space.

        The seen set contains up to O(vk) entries.

        Overall, the space complexity is O(v + e + ek + vk).
    """

    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # build adjacency list
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        # encode as (path cost, longest consecutive seq, curr node)
        pq = [(0, 1, 0)]
        seen = set()
        while pq:
            cost, seq, curr = heapq.heappop(pq)

            if (curr, seq) in seen:
                continue

            seen.add((curr, seq))

            # found valid path
            if curr == n - 1 and seq <= k:
                return cost

            # explore neis
            for nei, w in adj[curr]:
                newCost = cost + w
                newSeq = seq + 1 if labels[nei] == labels[curr] else 1

                # prune invalid paths early
                if newSeq > k or (nei, newSeq) in seen:
                    continue

                heapq.heappush(pq, (newCost, newSeq, nei))

        # no valid paths exist
        return -1

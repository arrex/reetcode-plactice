from collections import defaultdict, deque
from typing import List


class Solution:
    """
    Intuition:
        We use a BFS approach to solve this problem. We can model the
        graph where each element is connected to its adjacent elements
        and also its duplicates.

        Then, in our exploration loop, we add the previous/next elmts
        to the queue plus all the duplicates. We use a seen array to
        make sure we don't explore positions we have visited already.
        We also register neighbours immediately in the seen set to
        prevent appending them multiple times in a single iteration.

    Runtime:
        Building the adjacency list takes O(n) time.

        The BFS loop takes O(V + E) time where V is the num of vertices
        and E the num of edges. Here, we have up to n edges (all dupes)
        and up to n vertices. This the BFS exploration takes O(n) time.

        Overall, we have a O(n) time complexity.

    Memory:
        We have up to n edges, so O(n) for the adjacency list.

        We have n vertices, so the BFS queue takes up to O(n) and the
        seen set O(n) as well.

        Overall, O(n) space.
    """

    def minJumps(self, arr: List[int]) -> int:
        N = len(arr)
        adj = defaultdict(list)
        for i, n in enumerate(arr):
            adj[n].append(i)

        # starting pos
        q = deque([0])
        seen = {0}
        jumps = 0
        while q:
            for _ in range(len(q)):
                pos = q.popleft()
                num = arr[pos]

                # end condition
                if pos == N - 1:
                    return jumps

                # jump to prev ix
                if pos - 1 not in seen and pos - 1 >= 0:
                    q.append(pos - 1)
                    seen.add(pos - 1)

                # jump to prev ix
                if pos + 1 not in seen and pos + 1 < N:
                    q.append(pos + 1)
                    seen.add(pos + 1)

                for nei in adj[num]:
                    if nei not in seen:
                        q.append(nei)
                        seen.add(nei)
                del adj[num]

            jumps += 1

        # should never get here
        return jumps

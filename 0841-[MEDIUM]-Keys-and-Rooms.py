from collections import deque
from typing import List


class Solution:
    """
    Intuition:
        We can think of traversing the rooms as a classic DFS problem. The keys represent
        the nodes since we need a key to travel to a specific room. At the end, simply check
        if the number of visited rooms is equal to the total number of rooms.

    Runtime:
        O(|V| + |E|) where |V| is the number of rooms and |E| is the number of "edges"
        represented as keys here.

    Memory: O(n) where n is the number of nodes i.e. keys.

    Notes:
        Constraints specify at least 2 rooms, so we don't need to check that the length
        of the rooms array is 0.
    """

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Constraints specify at least 2 rooms
        numRooms = len(rooms)
        visited = set([0])

        # Init queue
        q = deque(rooms[0])

        while q:
            room = q.pop()
            visited.add(room)

            for key in rooms[room]:
                if key not in visited:
                    q.append(key)

        return len(visited) == numRooms

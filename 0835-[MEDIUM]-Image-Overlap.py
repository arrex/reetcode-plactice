from typing import List


class Solution1:
    """
    Intuition:
        Brute force approach. We make a list of coordinates for
        img1 and img2 to store all cells having value 1. Then,
        we take each pair of coordinates and compute the shift
        required between them. We then examine each possible
        shift and compute the overlap.

    Runtime:
        O(n^2) to compute the coords in img1, same for img2.

        O(n^2) to compute all possible shifts between coords1
        and coords2.

        O(n^3) to compute all possible image overlap scenarios
        since we have up to n^2 shifts and we examine each coord
        in coords1 for which there are up to n of.

        Overall, O(n^3) runtime.

    Memory:
        O(n) for coords1, same for coords2.

        O(n^2) to store all shifts in the hashset.

        Overall, O(n^2) memory.
    """

    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        N = len(img1)

        # get all coords where cell val is 1 in img1
        coords1 = []
        for r in range(N):
            for c in range(N):
                if img1[r][c] == 1:
                    coords1.append((r, c))

        # no possible overlap -- there are no 1's in img1
        if not coords1:
            return 0

        coords2 = []
        for r in range(N):
            for c in range(N):
                if img2[r][c] == 1:
                    coords2.append((r, c))

        shifts = set()
        for r1, c1 in coords1:
            for r2, c2 in coords2:
                dr, dc = r2 - r1, c2 - c1
                shifts.add((dr, dc))

        res = 0
        for dr, dc in shifts:
            curr = 0

            for r1, c1 in coords1:
                r2, c2 = r1 + dr, c1 + dc

                # out of bounds
                if r2 < 0 or r2 >= N or c2 < 0 or c2 >= N:
                    continue

                if img2[r2][c2] == 1:
                    curr += 1

            if curr > res:
                res = curr

        return res


class Solution2:
    """
    Intuition:
        We can optimize the brute force solution via hashing.

        We can save the computation of overlap by bucketing
        pairs of coordinates by the shift. Pairs of coordinates
        with the same shift are grouped together and we track
        their count.

    Runtime:
        O(n) to compute coords in img1 and img2.

        O(n^2) to bucket all pairs of coords by shift.

        O(n^2) to find the shift with the max overlap since
        there are at most n^2 shifts.

        Overall, O(n^2) runtime which better than O(n^3) from the
        previous solution.

    Memory:
        O(n) for coords1 and coords2.

        O(n^2) for the shifts hashmap.

        Overall, O(n^2) memory.
    """

    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        N = len(img1)

        # get all coords where cell val is 1 in img1
        coords1 = []
        for r in range(N):
            for c in range(N):
                if img1[r][c] == 1:
                    coords1.append((r, c))

        # no possible overlap
        if not coords1:
            return 0

        coords2 = []
        for r in range(N):
            for c in range(N):
                if img2[r][c] == 1:
                    coords2.append((r, c))

        # key = (dr, dc) i.e. row and col-wise cartesian dists, val = cnt
        shifts = {}
        for r1, c1 in coords1:
            for r2, c2 in coords2:
                dr, dc = r2 - r1, c2 - c1
                shifts[(dr, dc)] = shifts.get((dr, dc), 0) + 1

        return max(shifts.values()) if shifts else 0

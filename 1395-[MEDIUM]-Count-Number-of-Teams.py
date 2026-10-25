from collections import Counter


class Solution:
    """
    Intuition:
        Our BITs will track the frequency of each elmt.

        The insight here is the need to init 2 BITs. One of them tracks the elmts
        we have encountered and the other tracks elmts remaining. This way, we
        can efficiently satisfy the queries like elmts to lhs that are smaller/greater
        and elmts to rhs that are smaller/greater.

        At each elmt, we decrement the BIT tracking remaining frequencies and increment
        the BIT tracking seen frequencies. We then query for both cases to count num
        of teams.

    Runtime:
        O(n) to find max elmt in input arr.

        O(n) to init each BIT.

        O(n log n) to populate the BIT tracking remaining cnts.

        O(n log n) to find all valid teams.

        Overall, O(n log n) runtime.

    Memory:
        O(n) for each BIT.

        O(n) for the counter dictionary.

        Overall, O(n) memory.
    """

    class BIT:
        def __init__(self, size: int):
            self.bit = [0] * (size + 1)
            self.size = size

        def add(self, ix: int, val: int):
            while ix <= self.size:
                self.bit[ix] += val
                ix += ix & -ix

        def sum(self, ix: int) -> int:
            tot = 0
            while ix > 0:
                tot += self.bit[ix]
                ix -= ix & -ix
            return tot

    def numTeams(self, rating: list[int]) -> int:
        # BIT slot is keyed on rating
        # value is the freq of soldiers w that rating
        # we init 2 BITs: 1 remaining (decr) and one tracking seen (incr)
        size = max(rating)
        seen = self.BIT(size)
        remaining = self.BIT(size)

        for r, cnt in Counter(rating).items():
            remaining.add(r, cnt)

        res = 0
        for r in rating:
            # update BITs
            seen.add(r, 1)
            remaining.add(r, -1)

            # rating[i] < rating[j] < rating[k]
            lhs = seen.sum(r - 1)
            rhs = remaining.sum(size) - remaining.sum(r)

            res += lhs * rhs

            # rating[i] > rating[j] > rating[k]
            lhs = seen.sum(size) - seen.sum(r)
            rhs = remaining.sum(r)

            res += lhs * rhs

        return res

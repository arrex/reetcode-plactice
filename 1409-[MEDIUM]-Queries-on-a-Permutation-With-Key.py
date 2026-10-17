class Solution1:
    """
    Intuition:
        We can create an array to simulate each query. This is admittedly
        a brute force approach.

    Runtime:
        Suppose there are n queries. For each query, we have to find the
        index of the element which takes linear time O(n) and shift the
        array which also takes linear time. Thus, each query takes O(n + n)
        ~ O(n) time. With n queries, this gives us a runtime of O(n^2).

    Memory:
        We need O(n) space for the permutation array p.
    """

    def processQueries(self, queries: list[int], m: int) -> list[int]:
        p = [i for i in range(1, m + 1)]

        res = []
        for q in queries:
            ix = p.index(q)
            res.append(ix)
            p = [p[ix]] + p[:ix] + p[ix + 1 :]

        return res


class Solution2:
    """
    Intuition:
        We can use a binary indexed tree to make querying more efficient. The
        intuition behind this optimization is asking ourselves how we can make
        shifting the elmt to the front of the arr more efficient and how we
        can retrieve its "rank" (i.e. the num of elmts preceeding it which is
        equivalent to its position) more efficiently.

        The insight is that we can assign the value of 1 to an occupied slot
        and then compute the prefix sum to answer the rank. We will see below
        what an occupied slot means.

        There are 2 types of slots in our BIT: occupied and unoccupied. We
        allocate an unoccipied slot for each query and place these at the head
        of our BIT's array. We then append an occupied slot for each elmt in
        the permutation array of length m.

        The reason for having unoccupied slots is that we can simply use the
        BIT's add/update method to decrement the value at the old slot by 1
        and then increment the value at its new slot by 1 to represent a move.
        This gives us efficient shifting for each query. Each prefix sum query
        is also sped up using this BIT data structure.

    Runtime:
        We have n queries. Each query requires a prefix sum operation which takes
        O(log n) time, and 2 add/udpate operations which takes O(2 * log n) ~ O(log n)
        time.

        Overall, our runtime is O(n log n).

    Memory:
        The array stored in the BIT takes O(m + n) space.

        The hashmap we use to map elmts to their slot takes O(m).

        Thus, our memory complexity is O(m + n).
    """

    class BIT:  # Binary Indexed Tree
        def __init__(self, size: int):
            self.size = size
            # +1 bc 1-indexed
            self.bit = [0] * (self.size + 1)

        def add(self, ix: int, val: int) -> None:
            while ix < self.size:
                self.bit[ix] += val
                ix += ix & -ix  # add last set bit

        def sum(self, ix: int) -> int:
            sum = 0

            while ix > 0:
                sum += self.bit[ix]
                ix -= ix & -ix  # flip last set bit

            return sum

    def processQueries(self, queries: list[int], m: int) -> list[int]:
        # init permutation arr
        p = [i for i in range(1, m + 1)]

        n = len(queries)
        m = len(p)

        # build binary indexed tree
        # size = num of queries (n) + size of permutation arr (m)
        bit = self.BIT(n + m)

        # initially, first n + 1 slots are unoccupied
        # populate 1 in remaining to represent occupied
        for i in range(n + 1, bit.size):
            bit.add(i, 1)

        # build hashmap of val -> slot in BIT
        hmap = {v: k + n + 1 for k, v in enumerate(p)}

        # process all queries
        res = []
        for ix, q in enumerate(queries):
            # fetch slot number for this value
            slot = hmap[q]

            # find prefix sum (i.e. num of elmts preceeding it)
            prefix = bit.sum(slot - 1)
            res.append(prefix)

            # update value slot number
            newSlot = n - ix
            hmap[q] = newSlot

            # perform udpates to BIT
            bit.add(newSlot, 1)  # move elmt to front
            bit.add(slot, -1)  # remove it from old slot

        return res

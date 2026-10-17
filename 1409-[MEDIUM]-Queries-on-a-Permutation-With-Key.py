class Solution:
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

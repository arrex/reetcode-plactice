from math import comb


class Solution:
    """
    Intuition:
        We can model this problem using the stars and bars theorem from
        combinatorics.

        Stars represent objects we need to distribute among the buckets.
        In this problem, that's the extra unit intervals that we can
        allocate to gaps.

        Bars represent boundaries separating buckets. In this problem,
        our buckets are what we can "attribute more unit intervals" to
        i.e. extend. We can either extend either of the k segments or
        any of the k + 1 gaps.

        For example, if we have n = 4 and k = 2, we have a total of 3
        unit intervals, 2 of which we must reserve, leaving 1 extra
        unit interval we can use to extend either of the 2 segments or
        any of the 3 gaps. The encoding below illustrates the general
        idea:

        G = gap
        L = segment

        str = G, L, G, L, G

        Since a gap can be empty i.e. a bucket can be empty, we use the
        formula (stars + bars) choose (bars) (Theorem 2 from
        https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics)).

    Runtime:
        The biggest term to compute is fact(stars + bars), where
        stars = n - 1 - k
        bars = 2 * k
        stars + bars = n - 1 - k + 2 * k = n + k - 1

        Thus, runtime is bounded by O(fact(n + k)).

    Memory:
        O(1).
    """

    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        # n points create n - 1 unit intervals
        # reserve one unit interval for each of the k required segments
        # leaving n - 1 - k extra units to distribute
        stars = n - 1 - k
        # we have k reserved segments, which means we have k + 1 gaps
        # extra unit intervals can be distributed to either extending
        # any of the k segment buckets or any of the k + 1 gap buckets
        bars = 2 * k
        # stars and bars with empty buckets allowed:
        # (stars + bars) choose (bars)
        return comb(stars + bars, bars) % MOD

from collections import defaultdict, deque
from typing import List


class Solution:
    """
    Intuition:
        We start off by computing all primes up to the upper bound
        specified by the constraint. Using the sieve of Eratosthenes
        approach.

        Then, we use the fact that we need to compute the "minimum
        amount of jumps" to infer a BFS solution. To do so, we need
        to model our graph.

        The edges we create map from a prime factor to all the indices
        of values having that prime as a factor. Then, we use a standard
        BFS traversal. We need to maintain a visited list of nodes to
        prevent infinite cycles/redundant paths in our traversal. At each
        step, we need to add the adjacent jumps to our BFS deque and
        all indices if the current value is prime.

    Runtime complexity:
        Constructing the list of all primes up to MAX_VAL takes O(M * log log M)
        where M = MAX_VAL.

        The cost of one get_prime_factors call is at most O(log n) since we
        divide by at least 2 at each step. This makes constructing our edges
        cost O(n * log n). Note that this upper bound is very loose.

        For BFS, the runtime is O(V + E) where V and E are the cardinalities
        of vertices and edges respectively. Here, we have n vertices. Theoretically,
        a number has at most (log N / log log N) prime factors. With our upper
        bound of 10^6, this yields ~7. So we have O(7 * n) ~ O(n) edges effectively.
        This gives us a BFS runtime of O(n + n) ~ O(n).

        Overall, we have a runtime complexity dominated by O(n * log n)

    Memory complexity:
        We store smallest prime factor per number in spf array, so O(n) space.

        Number has at worst ~7 prime factors, so O(1) space per number. Given
        primeMap maps numbers to factors, this gives us O(7 * n) ~ O(n) space.

        The seen array of BFS takes O(n) space. The deque fits at most all
        nodes at once, so also O(n).

        Overall, O(n) space complexity.
    """

    def minJumps(self, nums: List[int]) -> int:
        MAX_VAL = 10**6  # specified by constraint

        # watch https://www.youtube.com/results?search_query=spf+sieve+algorithm for more info
        spf = list(range(MAX_VAL + 1))
        for i in range(2, int(MAX_VAL**0.5) + 1):
            if spf[i] == i:  # i is prime
                for j in range(i * i, MAX_VAL + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        def get_prime_factors(n):
            factors = set()

            while n > 1:
                p = spf[n]  # extract smallest prime factor
                factors.add(p)
                n //= p

                # skip duplicates
                while n > 1 and n % p == 0:
                    n //= p

            return factors

        N = len(nums)
        # map of edges:
        # prime factor -> list of indices of vals having that prime as a factor
        primeMap = defaultdict(list)

        # build edges
        for i, n in enumerate(nums):
            factors = get_prime_factors(n)
            for f in factors:
                primeMap[f].append(i)

        # bfs
        q = deque([0])
        seen = [False] * N
        seen[0] = True
        jumps = 0

        while q:
            for _ in range(len(q)):
                ix = q.popleft()
                if ix == N - 1:
                    return jumps

                n = nums[ix]

                # jump to adjacent nodes
                if not seen[ix + 1] and ix + 1 < N:
                    q.append(ix + 1)
                    seen[ix + 1] = True
                if not seen[ix - 1] and ix - 1 >= 0:
                    q.append(ix - 1)
                    seen[ix - 1] = True

                # if prime, check for edges via primeMap to teleport
                if spf[n] == n:
                    targets = primeMap.pop(n, [])
                    for jx in targets:
                        if not seen[jx]:
                            q.append(jx)
                            seen[jx] = True

            jumps += 1

        # should never get here
        return -1

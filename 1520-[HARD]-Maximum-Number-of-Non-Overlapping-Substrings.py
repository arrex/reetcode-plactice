from collections import Counter, deque
from math import inf


class Solution1:
    """
    Intuition:
        Brute force approach. This soln TLE's...

        Start by forming every possible substr and storing only the valid
        ones in a list of candidates.

        Then, we sort the candidates by end ix to make sure we process them
        in order.

        Lastly, we take each candidate and anchor it as our first selection.
        We then check how many remaining non-overlapping substrings we can
        select in our candidates and return the maximum result.

    Runtime:
        O(n) to compute the frequency counter.

        O(n * n * n) ~ O(n^3) to go through every possible substr and
        validate it.

        O(26^2 log 26^2) ~ O(1) to sort all the candidates as we have
        at most up to 26^2 valid substrs (26 chars with diff start/end
        indices in the worst case i.e. 26^2 possible candidates).

        O(n * n) ~ O(n^2) to find the maximum num of non-overlapping substrs as
        we have up to 26^2 * n ~ n candidates with the longest one being of len n.

        Overall, O(n^3) runtime.

    Memory:
        O(n) for the frequency counter.

        O(26^2 * n) ~ O(n) for the candidates array.

        O(n) for the res array.

        Overall, O(n) memory.
    """

    def maxNumOfSubstrings(self, s: str) -> list[str]:
        N = len(s)
        freq = Counter(s)
        candidates = []

        # go thru every possible substr -- n^2
        for i in range(N):
            for j in range(i, N):
                currFreq = Counter(s[i : j + 1])

                valid = True
                for c, f in currFreq.items():
                    # substr is invalid
                    if f != freq[c]:
                        valid = False

                if valid:
                    candidates.append((i, j, s[i : j + 1]))

        # sort candidates by end ix
        candidates = sorted(candidates, key=lambda x: x[1])

        # start at every substr and count num of non-overlapping
        res = []
        for i, (_, iend, isubstr) in enumerate(candidates):
            currIx = iend
            curr = [isubstr]

            for jstart, jend, jsubstr in candidates[i + 1 :]:
                if jstart > currIx:
                    curr.append(jsubstr)
                    currIx = jend

            if len(curr) > len(res):
                res = curr

        return res


class Solution2:
    """
    Intuition:
        We can build on top of the previous soln. The idea of maintaining a freq
        counter is good. On top, we can store the first and last ix of each char.

        The idea is to process each char, look at its start/end indices, and expand
        them if there is any char within the curr start/end that starts/ends outside
        the boundary. Since we might need to expand more than once, we maintain a
        queue to this effect.

        Note that a substr is valid if the total cnt of occurrences equals its
        length i.e. tot = r - l + 1. Upon finding a valid substr, we clear the
        queue to satisfy the non-overlapping condition. Clearing the queue essentially
        forces the next substr to avoid expanding with any of the previously
        processed chars.

    Runtime:
        O(n) to count frequencies, compute first/last indices.

        We have 26 distinct possible chars, each one's frequency is processed up to
        once. In the case we find a valid substr, it takes O(r - l + 1) time to slice
        the string. Since each valid substr is non-overlapping, we essentially
        process each char in s up to once only, meaning O(26 * n) ~ O(n) time.

        Overall, O(n) runtime.

    Memory:
        O(n) for the frequency counter and first/last ix maps.

        O(26) ~ O(1) for the queue.

        Overall, O(n) memory complexity.
    """

    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # count occurrences of each char
        freq = Counter(s)
        # store first ix of each char
        first = {c: s.find(c) for c in freq}
        # store last ix of each char
        last = {c: s.rfind(c) for c in freq}

        res = []
        # if q has elmts, this means we need to expand curr substr
        q = deque()

        # note: this soln works bc freq implicitly stores chars in
        # order of starting ix, so we process them in order of appearance
        for c in freq:
            # append char's first and last ix and its cnt
            # to the FRONT of the q
            q.appendleft((first[c], last[c], freq[c]))

            l, r = inf, -inf
            tot = 0

            # expand curr substr
            for fst, lst, cnt in q:
                tot += cnt
                l = min(l, fst)
                r = max(r, lst)

                # found a valid substr if sum of occurrences of chars
                # stored in tot equals its len
                if tot == r - l + 1:
                    break

            if tot == r - l + 1:
                res.append(s[l : r + 1])
                # clear the q to avoid overlapping substrs
                q.clear()

        return res

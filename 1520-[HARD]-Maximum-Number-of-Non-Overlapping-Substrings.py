from collections import Counter


class Solution:
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

        O(n * n * 26) ~ O(n^2) to go through every possible substr and
        validate it.

        O(n^2 log n^2) to sort all the candidates as we have at most up
        to n^2 valid substrs.

        O(n^2 * n) to find the maximum num of non-overlapping substrs as
        we have up to n^2 candidates with the longest one being of len n.

        Overall, O(n^3) runtime.

    Memory:
        O(n) for the frequency counter.

        O(n^2) for the candidates array.

        O(n) for the res array.

        Overall, O(n^2) memory.
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

import math
from collections import Counter, defaultdict


class Solution:
    """
    Intuition:
        Use a sliding window with two pointers (l, r) and frequency counts.
        Expand r to include chars until the window covers all requirements in t
        (tracked by 'have' vs 'need' using a Counter for t). Once covered,
        shrink from the left to drop unnecessary chars and record the shortest
        valid window. Repeat until r reaches the end.

        We encode requirements via 'need' and 'have' to avoid having to traverse the
        counter every single time we modify the window which would add a factor of
        O(|t|) to our runtime since we would need to cross-check with the counter every
        time we update our window.

    Runtime:
        We need O(|t|) time to build the counter for the string t. Each index in s is
       processed at most twice (once to add it to the window, once if the window is
       contracted) so the runtime for that is O(|s|). Overall, we obtain O(|s| + |t|).

    Memory:
        O(|s| + |t|) since we have a frequency hashmap for the window and a counter for
        t respectively. The problem states we only have lowercase English characters, so
        the complexity technically simplifies to O(1) since the number of letters is
        bounded by 26.
    """

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        counterT = Counter(t)
        need = len(counterT)

        l, r = 0, 0
        have = 0
        window = defaultdict(int)
        shortest, res = math.inf, ""

        while r < len(s):
            window[s[r]] += 1

            if window[s[r]] == counterT[s[r]]:
                have += 1

            while have == need:
                if r - l + 1 < shortest:
                    shortest = r - l + 1
                    res = s[l : r + 1]

                window[s[l]] -= 1

                if window[s[l]] < counterT[s[l]]:
                    have -= 1

                l += 1

            r += 1

        return res

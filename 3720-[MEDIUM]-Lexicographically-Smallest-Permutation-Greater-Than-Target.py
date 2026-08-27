class Solution:
    """
    Intuition:
        We maintain a counter that tracks the char-wise frequency difference
        between the inputs s and target. This counter array represents the
        pool of available chars we have to construct our permutation.

        A negative value in this counter array means that we are missing a
        given char in s to make up target i.e. a deficit. A positive value
        means that s has more of a given char than target i.e. a surplus.

        We then iterate through the target string from right to left. Why?
        Because the lexicographically smallest permutation requires us to
        make a change to the rightmost position.

        On each iteration, we give back the char we are at in target back
        to the available pool. We do so until there are no more deficits
        i.e. min(cnt) < 0 is false. No more deficits means that we can
        construct the prefix target[:i] with the available chars in cnt.

        Once we have found position i for which we can construct target[:i]
        with the available pool, we know this is the rightmost position
        where we can make a replacement. So, we scan the available pool
        to find the smallest larger char we can replace this position with.

        Once we make this replacement at position i, the permutation is
        already lexicographically larger. So we want the suffix to be as
        small as possible. We construct the suffix by greedily appending
        smallest chars to largest.

        If we are never able to get rid of deficits in cnt or we can't
        find a lexicographically larger char, then we simply return an
        empty string.

    Runtime:
        O(n) to construct the cnt array.

        O(26 * n) ~ O(n) since the outer loop has n iterations, checking
        min(cnt) < 0 takes O(26) and finding the larger char also takes
        O(26).

        Overall, O(n) runtime.

    Memory:
        O(26) for the cnt array.
    """

    def lexGreaterPermutation(self, s: str, target: str) -> str:
        # tracks how many more copies of
        # char x are in s than in target
        cnt = [0] * 26
        for c1, c2 in zip(s, target):
            cnt[ord(c1) - ord("a")] += 1
            cnt[ord(c2) - ord("a")] -= 1

        t = list(target)
        # go right to left since we want to find rightmost
        # position where we can make the permutation bigger
        for i in range(len(s) - 1, -1, -1):
            # give char at position i in target string back
            # to available pool `cnt`
            charIx = ord(t[i]) - ord("a")
            cnt[charIx] += 1

            # if min(cnt) < 0, then we cannot construct prefix
            # target[:i] from the available pool of chars `cnt`
            # as some char is still missing
            if min(cnt) < 0:
                continue

            # we can construct the prefix target[:i] with the
            # available pool. so we find the smallest larger
            # char at position `i` to make the permutation larger
            for j in range(charIx + 1, 26):
                if cnt[j] > 0:
                    # use this larger char at position `i`
                    cnt[j] -= 1
                    t[i] = chr(ord("a") + j)

                    # at this point, our permutation is larger. so
                    # we can simply greedily construct the smallest
                    # string with the remaining chars
                    minString = []
                    for k in range(26):
                        minString.append(chr(ord("a") + k) * cnt[k])

                    # join the prefix (including the replacement larger
                    # char -- hence i + 1 slicing) and the min string
                    # suffix
                    return "".join(t[: i + 1]) + "".join(minString)

        # no possible larger permutation
        return ""

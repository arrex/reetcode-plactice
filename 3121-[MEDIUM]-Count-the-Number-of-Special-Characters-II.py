class Solution1:
    """
    Intuition:
        Brute force approahc. Linearly scan the input word and use
        bitmaps to track state. State transitions are a bit messy,
        but the idea is to transition the 'upper' bitmap based on
        if we have encountered a lowercase variant of that letter.
        The lowercase letters can also be invalidated when we
        encounter a lower letter after its upper variant or if we
        encounter the lower variant once the letter was previously
        invalidated.

    Runtime:
        O(n), one pass.

    Memory:
        O(1).
    """

    def numberOfSpecialChars(self, word: str) -> int:
        # 0 = initial state, 1 = encountered, -1 = invalid
        lower = [0] * 26
        upper = [0] * 26

        for c in word:
            ix = ord(c.lower()) - ord("a")

            if c.islower():
                # happy path -- encounter lower
                if lower[ix] == 0:
                    lower[ix] = 1
                # already encountered uppercase, invalidate char
                elif upper[ix] == 1:
                    lower[ix] = -1
                    upper[ix] = 0
            else:  # upper case char
                # happy path -- lower encountered before upper
                if lower[ix] == 1:
                    upper[ix] = 1
                # either char is invalid or no lower instance encountered
                else:
                    lower[ix] = -1

        return sum(upper)


class Solution2:
    """
    Intuition:
        We store the last occurrence of the lower variant and the first occurrence
        of the upper variant. At the end, we check that the last lower does not
        overlap with the first upper.

    Runtime:
        O(n) to consume the input word.

    Memory:
        O(1) for the arrays.
    """

    def numberOfSpecialChars(self, word: str) -> int:
        lastLowerIx = [-1] * 26
        firstUpperIx = [-1] * 26

        for pos, c in enumerate(word):
            cIx = ord(c.lower()) - ord("a")

            if c.islower():
                lastLowerIx[cIx] = max(lastLowerIx[cIx], pos)
            else:
                if firstUpperIx[cIx] == -1:
                    firstUpperIx[cIx] = pos

        # note condition requires last lower < first upper AND that we actually encountered a lower
        return sum([lL < fU and lL != -1 for lL, fU in zip(lastLowerIx, firstUpperIx)])

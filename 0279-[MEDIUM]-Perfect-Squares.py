from math import sqrt


class Solution:
    """
    Intuition:
        We obviously need to have a pool of squares to choose from, meaning
        we need to compute some squares. However, note that we do not need
        any squares that are greater than the input `n`.

        We create an array `diffs` to hold the current "level" of the decision
        tree. Each element in the diffs array represents a path we have taken
        based on the square we subtracted from the previous value. The `turn`
        counter keeps track of the "level" which is also the number of squares
        we have currently chosen.

        The termination condition is when we see 0 in the `diffs` array, which
        means that we have found a valid combination.

    Runtime:
        O(sqrt(n)) to compute squares.

        O(n) until 0 appears in `diffs` in the worst case (i.e. when input n
        can only be composed of 1's).

        Overall, O(n) runtime.

    Memory:
        O(n) since values in `diffs` always range between 0 and `n` inclusive.
    """

    def numSquares(self, n: int) -> int:
        # don't need squares > n
        squares = [i**2 for i in range(1, int(sqrt(n) + 1))]
        diffs = set({n - s for s in squares})
        turn = 1

        while 0 not in diffs:
            turn += 1
            newDiffs: set[int] = set()

            for s in squares:
                for d in diffs:
                    if d - s >= 0:
                        newDiffs.add(d - s)

            diffs = newDiffs

        return turn

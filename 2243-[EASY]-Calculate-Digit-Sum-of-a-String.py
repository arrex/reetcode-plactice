class Solution:
    """
    Intuition:
        Brute force it, given that constraints are small.

    Runtime:
        There are roughly O(log_k n) rounds where n is the length of
        the input string `s`. The overall amortized runtime is O(n)
        since we process every digit in the first round, and subsequent
        rounds have less work.

    Memory:
        O(n) for the intermediate `groups` array the input's components.
    """

    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            groups = [s[i : i + k] for i in range(0, len(s), k)]

            for i, g in enumerate(groups):
                digitSum = sum(int(d) for d in g)
                groups[i] = str(digitSum)

            s = "".join(groups)

        return s

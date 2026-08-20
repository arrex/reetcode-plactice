class Solution1:
    """
    Intuition:
        Use a 2 ptr approach to find palindromes. The key thing to note
        is that a palindrome can either be even in length or odd. We
        iterate through every index of the input string and search for both
        even and odd palindromes.

    Notes:
        There exists a DP approach too that is covered in the solution below.

    Runtime: O(n * k) where k is the length of the longest palindromic substring

    Memory: O(1)
    """

    def countSubstrings(self, s: str) -> int:
        res = 0

        # Count all odd palindromes
        for i in range(len(s)):
            # Odd palindromes
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            # Even palindromes
            if i < len(s) - 1:
                l, r = i, i + 1

                while l >= 0 and r < len(s) and s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1

        return res


class Solution2:
    """
    Intuition:
        Finding palindromes is something that satisfies the conditions for a
        DP solution well. We have the optimal substructure property where a
        larger substring is palindromic only if the smaller substring composing
        it is palindromic too. It also satisfies the overlapping subproblems
        property since subproblems are repeatedly used to solve overlaps.

    Notes:
        Requires more memory than previous solution

        Also runs slower due to requiring an extra pass to build base cases.

        Can optimize by breaking from checking subproblems as soon as
        2 different characters are encountered.
    """

    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        # Let dp[ix][jx] be True if the substring starting at ix and
        # ending at jx inclusivelu is palindromic
        dp = [[False] * n for _ in range(n)]

        # Build base cases
        for i in range(n):
            # Character itself is palindromic by def
            # Odd palindrome base case (length 1)
            dp[i][i] = True
            res += 1

            # Check even palindrome base case (length 2)
            if i < n - 1 and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                res += 1

        # Bottom-up, starting at length 3
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                start, end = i, i + length - 1

                # Check subproblem
                if dp[start + 1][end - 1] and s[start] == s[end]:
                    dp[start][end] = True
                    res += 1

        return res

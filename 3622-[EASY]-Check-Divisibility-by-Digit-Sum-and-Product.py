class Solution:
    """
    Intuition:
        Compute digit sum and product.

        Sum those two and check modulo division.

    Runtime:
        O(log_10(n)) ~ O(log n) since computing digit sum and product
        scales with respect to magnitude of input `n`.

    Memory:
        O(1).
    """

    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_prod = 1

        copy = n
        while copy:
            rem = copy % 10

            digit_sum += rem
            digit_prod *= rem

            copy //= 10

        return n % (digit_sum + digit_prod) == 0

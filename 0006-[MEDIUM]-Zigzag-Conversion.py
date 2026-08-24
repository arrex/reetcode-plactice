class Solution1:
    """
    Intuition:
        We generate the cycle of row numbers to iterate through. For example, if we have 3 rows, the cycle would
        array would contain [0, 1, 2, 1]. This way, we can use modulo math to increment the index when traversing
        the cycle array to wrap around and come back to 0 after the last 1.

        Then, we use this logic and traverse the input string to feed each character into their appropriate row.
        After than, we simply concatenate everything.

    Runtime:
        O(N) where N is the length of the input string since we need to traverse it to assign each char and then
        concatenate everything.

    Memory:
        O(N) as well since each character of the input string needs to be stored in a row array.
    """

    def convert(self, s: str, numRows: int) -> str:
        cycle = [i for i in range(numRows)]
        cycle.extend(range(numRows - 2, 0, -1))

        rows = [[] for _ in range(numRows)]

        # curr tracks current index of whichever row we are at
        # in the cycle array
        curr = 0

        for char in s:
            rows[cycle[curr]].append(char)
            curr = (curr + 1) % len(cycle)

        res = ""

        for row in rows:
            res += "".join(row)

        return res


class Solution2:
    """
    Intuition:
        We can optimize our previous solution by realizing 2 things:

        1) If the numRows is 1 or if the length of the input string is less than or equal to the number
        of rows, then we can return the string as is.

        2) Instead of building a cycle array to hold the row numbers, we can use a direction variable 'dir'
        that will act as an incrementor. It can either be +1 or -1. We manage this dir variable according
        to the current row's value.

    Runtime:
        Same a Solution1.

    Memory:
        Same as Solution1.
    """

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        rows = [[] for _ in range(numRows)]
        # dir encodes direction of travel
        currRow, dir = 0, 1

        for char in s:
            rows[currRow].append(char)

            if currRow == 0:
                dir = 1

            if currRow == numRows - 1:
                dir = -1

            currRow += dir

        for i in range(len(rows)):
            rows[i] = "".join(rows[i])

        return "".join(rows)

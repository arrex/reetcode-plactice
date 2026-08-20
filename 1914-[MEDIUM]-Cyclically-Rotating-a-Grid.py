from typing import List


class Solution1:
    """
    Intuition:
        To compute the number of layers, we need to take the length of the
        SHORTER edge of the matrix.

        For each layer, we buid an array of coordinates and their respective
        values in counter-clockwise order. We then iterate through these
        arrays to perform all the rotations. Note that we add the shift 'k'
        to the current index when computing 'destIx' even though the problem
        states counter-clockwise rotation since the ordering of the arrays
        is already counter-clockwise.

    Runtime:
        Every cell is processed once and rotated up to one time which means
        O(m * n) runtime overall.

    Memory:
        Every cell's coordinates and value is stored once, meaning O(m * n)
        memory complexity.
    """

    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if k == 0:
            return grid

        M, N = len(grid), len(grid[0])
        layers = min(M, N) // 2

        # perform rotations per layer
        for layer in range(layers):
            # gather coordinates and respective vals in counter clockwise order
            coords = []
            vals = []

            # go down
            col = layer
            for row in range(layer, M - layer):
                coords.append((row, col))
                vals.append(grid[row][col])

            # go right
            row = M - layer - 1
            for col in range(layer + 1, N - layer):
                coords.append((row, col))
                vals.append(grid[row][col])

            # go up
            col = N - layer - 1
            for row in range(M - layer - 2, layer - 1, -1):
                coords.append((row, col))
                vals.append(grid[row][col])

            # go left
            row = layer
            for col in range(N - layer - 2, layer, -1):
                coords.append((row, col))
                vals.append(grid[row][col])

            # rearrange elmts
            L = len(coords)
            for i in range(L):
                destIx = (i + k) % L
                destX, destY = coords[destIx]
                # store destination value in tmp and shift curr value to it
                grid[destX][destY] = vals[i]

        return grid


class Solution2:
    """
    Intuition:
        Same general intuition as Solution 1 with some optimizations.

        Remove need to auxiliary memory to store coordinates. We can just
        traverse using same logic we build the 'vals' array storing values
        to populate array with rotated values.

        We compute the shift (k % L) in case k is very, very large. This
        avoids costly arithmetic.

        Pre-rotate all values to facilitate traversal of values when
        rotating a layer.

    Runtime:
        Same as Solution 1.

    Memory:
        Same as Solution 1.
    """

    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if k == 0:
            return grid

        M, N = len(grid), len(grid[0])
        layers = min(M, N) // 2

        # perform rotations per layer
        for layer in range(layers):
            # gather vals in counter clockwise order
            vals = []

            # go down
            col = layer
            for row in range(layer, M - layer):
                vals.append(grid[row][col])

            # go right
            row = M - layer - 1
            for col in range(layer + 1, N - layer):
                vals.append(grid[row][col])

            # go up
            col = N - layer - 1
            for row in range(M - layer - 2, layer - 1, -1):
                vals.append(grid[row][col])

            # go left
            row = layer
            for col in range(N - layer - 2, layer, -1):
                vals.append(grid[row][col])

            # rearrange elmts
            L = len(vals)
            shift = k % L  # in case k is very large
            rotated = vals[-shift:] + vals[:-shift]
            ix = 0

            # go down
            col = layer
            for row in range(layer, M - layer):
                grid[row][col] = rotated[ix]
                ix += 1

            # go right
            row = M - layer - 1
            for col in range(layer + 1, N - layer):
                grid[row][col] = rotated[ix]
                ix += 1

            # go up
            col = N - layer - 1
            for row in range(M - layer - 2, layer - 1, -1):
                grid[row][col] = rotated[ix]
                ix += 1

            # go left
            row = layer
            for col in range(N - layer - 2, layer, -1):
                grid[row][col] = rotated[ix]
                ix += 1

        return grid

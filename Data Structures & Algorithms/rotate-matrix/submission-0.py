class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # Key Data Structure: 2D Matrix (In-Place Transformation)

        # Step 1: reverse the matrix vertically (flip rows top-to-bottom)
        # this handles half of the rotation — turns "rotate 90° clockwise"
        # into "reverse then transpose"
        matrix.reverse()

        # Step 2: transpose the matrix — swap matrix[i][j] with matrix[j][i]
        # only need to swap the upper triangle (j > i) to avoid swapping twice
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Time Complexity:  O(n^2) — visit every cell once
        # Space Complexity: O(1) — modifies matrix in place, no extra structures
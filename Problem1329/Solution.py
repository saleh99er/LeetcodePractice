from typing import List

class Solution:
    """
    A matrix diagonal is a diagonal line of cells starting from some cell
    in either the topmost row or leftmost column and going in the bottom-right 
    direction until reaching the matrix's end. For example, the matrix 
    diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes 
    cells mat[2][0], mat[3][1], and mat[4][2].

    Given an m x n matrix mat of integers, sort each matrix diagonal in 
    ascending order and return the resulting matrix.

    Approach: Focus on one diagonal at a time: read their elements from 
    matrix, sort them, and restore them in that matrix.

    m := rows of matrix
    n := columns of matrix
    t := upper bound of longest diagonal = min(n,m)
    d := # of diagonals of matrix = m + n - 1
    Runtime complexity := O(d * tlogt)
    Space complexity := O(t) = O(min(n,m))
    Runtime: 84ms, faster than 73.46% of submissions

    """

    def matrixDiagonalSortCopy(src_mat, dst_mat, m, n, diag_index):
        # Load diagonal contents
        matrix_diagonal = []
        init_row = max(m-1-diag_index, 0)
        init_col = max(diag_index-m+1, 0)

        row = init_row
        col = init_col
        while(col < n and row < m):
            # print(row,col)
            matrix_diagonal.append(src_mat[row][col])
            row += 1
            col += 1

        # Sort them
        matrix_diagonal.sort()
        # print(matrix_diagonal)

        # Store sorted elements in destination matrix
        row = init_row
        col = init_col
        i = 0
        while(col < n and row < m):
            dst_mat[row][col] = matrix_diagonal[i]
            row += 1
            col += 1
            i += 1


    def init2DArray(m,n):
        result = []
        for row_index in range(m):
            row = []
            for col_index in range(n):
                row.append(0)
            result.append(row)
        return result

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = 0 if len(mat) == 0 else len(mat[0])
        diags = m + n - 1
        result = Solution.init2DArray(m,n)
        for diag_index in range(diags):
            Solution.matrixDiagonalSortCopy(mat, result, m, n, diag_index)
        return result
        
        
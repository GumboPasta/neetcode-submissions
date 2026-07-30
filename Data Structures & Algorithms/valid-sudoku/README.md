# Valid Sudoku

**Difficulty:** Medium

Given a 9x9 Sudoku board partially filled in, determine whether the filled cells so far satisfy the Sudoku rules: each row, each column, and each of the nine 3x3 sub-boxes must contain no repeated digits from 1 through 9. Empty cells are represented by a period and are ignored.

## Example 1

Input: a 9x9 board where row one is [1, 2, ., ., 3, ., ., ., .] and the rest follows standard Sudoku formatting with no conflicting digits
Output: true

## Example 2

Input: the same board as above, but with an additional 1 placed in row two, column one, conflicting with the 1 already in row one
Output: false

Constraints: the board is always 9x9, and only the filled cells need to be validated.

Full problem statement: https://neetcode.io/problems/valid-sudoku

# Lowest Common Ancestor of a BST

**Difficulty:** Medium

Given the root of a binary search tree and two of its nodes, find and return the lowest node in the tree that has both nodes as descendants, where a node can be a descendant of itself.

## Example 1

Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 8
Output: 6

## Example 2

Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 4
Output: 2
Explanation: Node 2 is an ancestor of node 4 since a node is considered a descendant of itself.

Constraints: both p and q exist in the tree, and all node values are unique.

Full problem statement: https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree

# Construct Binary Tree from Preorder and Inorder Traversal

**Difficulty:** Medium

Given two integer arrays representing the preorder and inorder traversal of a binary tree with unique values, rebuild the tree and return its root node.

## Example 1

Input: preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
Output: [3, 9, 20, null, null, 15, 7]
Explanation: Node 3 is the root since it appears first in preorder; everything left of 3 in inorder forms the left subtree, and everything right forms the right subtree.

## Example 2

Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints: the node values in the tree are unique.

Full problem statement: https://neetcode.io/problems/binary-tree-from-preorder-and-inorder-traversal

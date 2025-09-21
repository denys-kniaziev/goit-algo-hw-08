# Woolf University. Basic Algorithms and Data Structures Course. Homework – Trees and Heaps

## Overview

This assignment covers working with binary search trees (BST), AVL trees, and heaps. You will implement algorithms to find the minimum value, compute the sum of values, and solve a cable-connection optimization problem using a heap.

---

## Task 1 – Minimum Value in a Tree

### Description

Write a function that finds the smallest value in a binary search tree (BST) or AVL tree.

### Requirements

* Use any implementation of a BST or AVL tree (from lecture notes or another source).
* Implement a function that traverses the tree and returns the minimum value.

### Evaluation Criteria

* Correct traversal logic (in a BST/AVL, the minimum is in the leftmost node).
* Function returns the correct minimum value.
* Clean and understandable implementation.

---

## Task 2 – Sum of All Values in a Tree

### Description

Write a function that computes the sum of all values stored in a BST or AVL tree.

### Requirements

* Use any implementation of a BST or AVL tree.
* Implement a function that recursively or iteratively traverses all nodes.
* Return the sum of all node values.

### Evaluation Criteria

* Correct aggregation of all node values.
* Works for both empty and non-empty trees.
* Efficient traversal and clean code.

---

## Task 3 – Cable Connection Optimization with a Heap

### Description

You are given several network cables of different lengths. You must connect them two at a time into one cable using connectors. The cost of connecting two cables equals the sum of their lengths, and the total cost is the sum of all connections. The goal is to find the order of combining that minimizes the total cost.

### Requirements

* Use a heap (priority queue) to repeatedly extract the two smallest cables and combine them.
* Continue until only one cable remains.
* Return the minimal total cost of combining.

### Evaluation Criteria

* Correct use of a heap to always combine the shortest cables first.
* Accurate calculation of total connection cost.
* Clear and efficient implementation.

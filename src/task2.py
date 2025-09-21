class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def sum_tree_values(root):
    """
    Calculate the sum of all values in a binary tree using recursive approach.
    
    Args:
        root: TreeNode - root of the tree
        
    Returns:
        int/float - sum of all values in the tree, 0 if tree is empty
    """
    if root is None:
        return 0
    
    # Current node value + sum of left subtree + sum of right subtree
    return root.value + sum_tree_values(root.left) + sum_tree_values(root.right)


def sum_tree_values_iterative(root):
    """
    Calculate the sum of all values in a binary tree using iterative approach with stack.
    
    Args:
        root: TreeNode - root of the tree
        
    Returns:
        int/float - sum of all values in the tree, 0 if tree is empty
    """
    if root is None:
        return 0
    
    total_sum = 0
    stack = [root]
    
    while stack:
        current = stack.pop()
        total_sum += current.value
        
        # Add children to stack for processing
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    
    return total_sum


def main():
    # Create a sample BST
    #       8
    #      / \
    #     3   10
    #    / \    \
    #   1   6    14
    #      / \   /
    #     4   7 13
    
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)
    root.right.right = TreeNode(14)
    root.right.right.left = TreeNode(13)
    
    print("Binary Search Tree sum of all values:")
    print(f"Recursive approach: {sum_tree_values(root)}")
    print(f"Iterative approach: {sum_tree_values_iterative(root)}")
    
    # Expected sum: 8 + 3 + 10 + 1 + 6 + 4 + 7 + 14 + 13 = 66
    
    # Test with empty tree
    print(f"Empty tree: {sum_tree_values(None)}")


if __name__ == "__main__":
    main()
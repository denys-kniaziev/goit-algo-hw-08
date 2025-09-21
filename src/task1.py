class TreeNode:
    def __init__(self, value) :
        self.value = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def find_min_value(root):
    """
    Find the minimum value in a Binary Search Tree.
    In BST, minimum value is always the leftmost node.
    
    Args:
        root: TreeNode - root of the BST
        
    Returns:
        int/float - minimum value in the tree, None if tree is empty
    """
    if root is None:
        return None
    
    # Keep going left until we find the leftmost node
    current = root
    while current.left is not None:
        current = current.left
    
    return current.value


def find_min_value_recursive(root):
    """
    Recursive implementation to find minimum value in BST.
    
    Args:
        root: TreeNode - root of the BST
        
    Returns:
        int/float - minimum value in the tree, None if tree is empty
    """
    if root is None:
        return None
    
    if root.left is None:
        return root.value
    
    return find_min_value_recursive(root.left)


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
    
    print("Binary Search Tree minimum value:")
    print(f"Iterative approach: {find_min_value(root)}")
    print(f"Recursive approach: {find_min_value_recursive(root)}")
    
    # Test with empty tree
    print(f"Empty tree: {find_min_value(None)}")


if __name__ == "__main__":
    main()
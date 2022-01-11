# Write a function to find the 2nd largest element in a binary search tree.

class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def find_second_largest(tree: BinaryTreeNode) -> BinaryTreeNode:
    result = tree
    while tree.right:
        result = tree
        tree = tree.right

    if not tree.left:
        return result

    result = tree.left
    while result.right:
        result = result.right

    return result


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# Where is the 2nd largest element of a BST going to be?
# First, to find the largest element, keep going down the right subtree in a BST.
# To find the 2nd largest element:
# - If the largest element is a leaf node, then the 2nd largest element has to be its parent.
# - If it has a left subtree, then the 2nd largest element has to be the largest elem in the left subtree.
# - If it has a right subtree, then it is not the largest element.
# O(n) worst case time complexity where n is number of nodes in the BST. Also O(h) if height known
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


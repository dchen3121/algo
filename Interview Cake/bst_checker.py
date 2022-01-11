# Write a function to check that a binary tree is a valid binary search tree.

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


def is_bst(node, lower_bound = float('-inf'), upper_bound = float('inf')):
    if not node:
        return True

    if node.value <= lower_bound or node.value >= upper_bound:
        return False

    return is_bst(node.left, lower_bound, min(upper_bound, node.value)) and is_bst(node.right, max(lower_bound, node.value), upper_bound)


def is_bst_in_order_traversal(node):
    stack = []
    last_num = float('-inf')

    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        if node.val < last_num:
            return False
        last_num = node.val
        if node.right:
            stack.append(node.right)

    return True




# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# it's not enough to just check left and right subtrees and make sure they're both BSTs - have to keep track of bounds as well
# O(n) time and space
# ----------------------------------------------------------------------------------------------------------------------------------------------------------



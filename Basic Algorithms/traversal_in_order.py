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


from typing import List


def in_order_traversal(tree: BinaryTreeNode) -> List[int]:
    result = []
    stack = []
    node = tree

    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        result.append(node.value)
        node = node.right

    return result

def in_order_traversal_recursive(tree: BinaryTreeNode) -> List[int]:
    result = []

    def traverse_help(node: BinaryTreeNode) -> None:
        if node.left:
            traverse_help(node.left)
        result.append(node.value)
        if node.right:
            traverse_help(node.right)

    traverse_help(tree)
    return result


tree_1 = BinaryTreeNode(1)
tree_2 = BinaryTreeNode(2)
tree_3 = BinaryTreeNode(3)
tree_4 = BinaryTreeNode(4)
tree_5 = BinaryTreeNode(5)
tree_6 = BinaryTreeNode(6)
tree_7 = BinaryTreeNode(7)

tree_2.left = tree_1
tree_2.right = tree_3
tree_6.left = tree_5
tree_6.right = tree_7
tree_4.left = tree_2
tree_4.right = tree_6

root = tree_4

print(in_order_traversal(root))
print(in_order_traversal_recursive(root))

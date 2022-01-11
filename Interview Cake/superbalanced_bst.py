# Write a function to see if a binary tree is "superbalanced" (a new tree property we just made up)
# A tree is "superbalanced" if the difference between the depths of any two leaf nodes is no greater than one.


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


def is_balanced_dfs(tree: BinaryTreeNode) -> bool:
    if not tree:
        return True

    depths = set()
    dfs_stack = [(tree, 0)]

    while dfs_stack:
        curr_node, curr_depth = dfs_stack.pop()
        if not curr_node.left and not curr_node.right:
            if curr_depth not in depths:
                if len(depths) == 2 or abs(depths[0] - curr_depth) > 1:
                    return False
                depths.add(curr_depth)
        else:
            if curr_node.left:
                dfs_stack.append((curr_node.left, curr_depth + 1))
            if curr_node.right:
                dfs_stack.append((curr_node.right, curr_depth + 1))

    return True


from collections import deque


def is_balanced_bfs(tree: BinaryTreeNode) -> bool:
    if not tree:
        return True

    bfs_queue = deque()
    bfs_queue.append(tree)

    while bfs_queue:
        curr_node = bfs_queue.popleft()
        if not curr_node.left and not curr_node.right:
            break
        if curr_node.left:
            bfs_queue.append(curr_node.left)
        if curr_node.right:
            bfs_queue.append(curr_node.right)

    for node in bfs_queue:
        if (node.left and (node.left.left or node.left.right)) or (node.right and (node.right.left or node.right.right)):
            return False

    return True

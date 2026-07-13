# Q15. Count the total number of nodes present in a binary tree.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


print("Total nodes:", count_nodes(root))
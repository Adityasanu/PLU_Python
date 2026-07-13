# Q16. Find and display all the leaf nodes of a binary tree.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)


def find_leaves(node, leaves):
    if node is None:
        return
    if node.left is None and node.right is None:
        leaves.append(node.data)
        return
    find_leaves(node.left, leaves)
    find_leaves(node.right, leaves)


leaves = []
find_leaves(root, leaves)
print("Leaf nodes:", leaves)
# Q14. Perform an Inorder Traversal on a binary tree.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)


def inorder(node, result):
    if node is None:
        return
    inorder(node.left, result)
    result.append(node.data)
    inorder(node.right, result)


result = []
inorder(root, result)
print("Inorder Traversal:", result)
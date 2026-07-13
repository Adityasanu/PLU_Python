# Q13. Create the following binary tree:
#         50
#        /  \
#       30   70
# Display the root, left child, and right child.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)

print("Root:", root.data)
print("Left child:", root.left.data)
print("Right child:", root.right.data)
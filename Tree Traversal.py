class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# def preOrderTraversal(node):
#     if node is None:
#         return
#     print(node.data, end=", ")
#     preOrderTraversal(node.left)
#     preOrderTraversal(node.right)

def InOrderTraversal(node):
    if node is None:
        return
    InOrderTraversal(node.left)
    print(node.data, end = " ")
    InOrderTraversal(node.right)
# def PostOrderTraversal(node):
#     PostOrderTraversal(node.left)
#     PostOrderTraversal(node.right)
#     print(node.data, end=" ")

root = TreeNode(12)
node6 = TreeNode(10)
node5 = TreeNode(8)
node3 = TreeNode(14)
node7 = TreeNode(19)
node18 = TreeNode(25)
node14 = TreeNode(13)
node11 = TreeNode(16)

root.left = node6
root.right = node7
node6.left = node5
node6.right = node14
node7.left = node3
node7.right = node11
node11.left = node18

InOrderTraversal(root)
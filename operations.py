# creating a treenode.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


# creating a Binary search tree.

root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right = TreeNode(12)
root.right.left = TreeNode(11)
root.right.right = TreeNode(15)

# traversals.
# inorder , preoreder , postorder.


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)


def preorder(root):
    if root is None:
        return
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val, end=" ")


# insertion.

def insert(root, val):
    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)

    return root

# searching operation.


def search(root, key):
    if root is None or root.val == key:
        return root

    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


# Example usage:
root = insert(root, 13)
# inorder(root)
# print()
# preorder(root)
# print()
# postorder(root)
# print()

result = search(root, 11)
if result is not None:
    print("Found:", result.val)
else:
    print("Not found")

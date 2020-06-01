
def path_exists(self, root, total):  # Solution time exceeded
    if root.left is None and root.right is None:
        if root.val == total:
            return True
        else:
            return False
    if root.left is None:
        return self.path_exists(root.right, total - root.val)
    elif root.right is None:
        return self.path_exists(root.left, total - root.val)
    else:
        return self.path_exists(root.left, total - root.val) or self.path_exists(root.right, total - root.val)


# @param A : root node of tree
# @param B : integer
# @return an integer
def hasPathSum(self, A, B):
    if self.path_exists(A, B):
        return 1
    else:
        return 0

#https://medium.com/@jooblee/check-if-two-binary-tree-are-isomorphic-967a9d08a19d
def isIsomorphic(n1, n2):
    # code here.
    if n1 == None and n2 == None:
        return True
    if not n1 or not n2:
        return False
    if n1.data != n2.data:
        return False
    lIdentical = isIsomorphic(n1.left, n2.left)
    rIdentical = isIsomorphic(n1.right, n2.right)
    lMirror = isIsomorphic(n1.left, n2.right)
    rMirror = isIsomorphic(n1.right, n2.left)
    if lIdentical and rIdentical or lMirror and rMirror:
        return True
    return False

def isMirror(self,n1, n2):
    if n1 == None and n2 == None:
        return True
    if not n1 or not n2:
        return False
    if n1.val != n2.val:
        return False
    lMirror = isMirror(n1.left, n2.right)
    rMirror = isMirror(n1.right, n2.left)
    if lMirror and rMirror:
        return True
    return False
def isSymmetric(self, root: TreeNode) -> bool:
    if root==None:
        return True
    if self.isIsomorphic(root.left,root.right):
        return True
    return False
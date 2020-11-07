def check_binary_search_tree_(root):
    current=root
    s,l=[],[]
    while True:
        if current is not None:
            s.append(current)
            current=current.left
        elif(s):
            current=s.pop()
            l.append(current.data)
            current=current.right
        else:
            break
    if sorted(set(l))==l:
        return True
    return False

def isBSTUtil(node, mini, maxi):

    # An empty tree is BST
    if node is None:
        return True

    # False if this node violates min/max constraint
    if node.data < mini or node.data > maxi:
        return False

    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (isBSTUtil(node.left, mini, node.data -1) and
          isBSTUtil(node.right, node.data+1, maxi))

def isBST(root,mi,ma):
    if root==None:
        return True
    if root.data<=mi or root.data>=ma:
        return False
    if isBST(root.left,mi,root.data) and isBST(root.right,root.data,ma):
        return True
    return False

 def isSubTreeLesser(root,data):
     if not root:
         return True
     if root.data<data and isSubTreeLesser(root.left,data) and isSubTreeLesser(root.right,data):
         return True
     return False

 def isSubTreeGreater(root,data):
     if not root:
         return True
     if root.data>data and isSubTreeGreater(root.right,data) and isSubTreeGreater(root.left,data):
         return True
     return False

 def check_binary_search_tree_1(root):
     #all the element in the left substree shuld be lesser than root and all the element in the right subtree should b greater than root
     if not root:
         return True
     if isSubTreeLesser(root.left,root.data) and isSubTreeGreater(root.right,root.data) and check_binary_search_tree_1(root.left) and check_binary_search_tree_1(root.right):
         return True
     return False
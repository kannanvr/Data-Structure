# User function Template for python3

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''


def height(root):
    '''
    :param root: root of the given tree.
    :return: Integer, height of the given binary tree
    {
        # Node Class:
        class Node:
            def _init_(self,val):
                self.data = val
                self.left = None
                self.right = None
    }
    '''
    # code here
    if root == None:
        return 0
    return max(1 + height(root.left), 1 + height(root.right))

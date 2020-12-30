package Tree

/*

def findPair(root,x):
    # code here
    s,h=[],{}
    current=root
    while True:
        if current != None:
            s.append(current)
            current=current.left
        elif(len(s)>0):
            current = s.pop()
            req=x-current.key
            if req in h:
                return 1
            else:
                h[current.key]=True
            current=current.right
        else:
            break
    return 0

*/

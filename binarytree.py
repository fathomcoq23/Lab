#binary search tree implementation

#creating a node
class Node:
    def __init__(self,data):
        self.data = data    #value to be added(to root or leaf)
        self.right=None     #right of my node
        self.left=None      #left of my node

class binary_search:
    def insert(self,root,data):
        if root==None:  #at start my root is empty,so value is none
            root =  Node(data)  #new root

        else:   #if a root already existed
            if data<=root.data: #if data is less that, insert to the left
                cur=self.insert(root.left,data) #recursively adding to the left
                root.left=cur   #first root to the left is cur

            else:   #data to right
                cur=self.insert(root.right,data)    #recursively adding leaves to the right
                root.right=cur  #right root's value
        return root

    def getHeight(self,root):
        #Write your code here
        count = 0
        if root:
            height_left = self.getHeight(root.left)
            height_right = self.getHeight(root.right)
            return (max(height_left,height_right) + 1)
        else:
            return -1

if __name__ == '__main__':
    T=int(input())
    myTree=binary_search()
    root=None #root is none here because no __init__ in binary_search class. only the methods ofthe class take in paramters
    for i in range(T):
        data=int(input())
        root=myTree.insert(root,data)
        height=myTree.getHeight(root)
        print(height)

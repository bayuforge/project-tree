#BAYUFORGE (C) MIT LICENSE CODE PROTECTED

#A class to create each node
class createNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.root = value

#A function to print each tree when it's has been initialized
def print_tree(node:createNode):
    if (node == None):
        print("---<empty>---")
        return
      
    #print each node with postorder traversal
    print(f"value: {node.root}")
    print("pos: left \n")
    print_tree(node.left)  #recursive for efficient performance
    print("pos: right \n")
    print_tree(node.right) #recursive for efficient performance

#Initialize the node
mytree_one = createNode(10)
mytree_two = createNode(11)
mytree_three = createNode(12)
mytree_four = createNode(13)
mytree_five = createNode(14)
mytree_five = createNode(15)

#Initialize the root and child
mytree_one.left = mytree_two
mytree_one.right = mytree_three
mytree_three.left = mytree_four
mytree_three.right = mytree_five

print_tree(mytree_one)


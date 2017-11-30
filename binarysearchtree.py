# binary search tree
# one path to each node
# only two children
# rules on how to add and remove from tree
# if tree is empty set new node to root
# if root exisists...ask if new value is greater or less than root
# iff new node is larger than root and no right child exists, it will be right child
# if new node is less than root and no left child exists, it will be the left child 
# if left/right child are taken, go down the tree and do the same logic
# every right child will be a greater or equal number than the parent node
# ever left child will be less than the parent node

import numpy.random as nprnd
from binarytree import Node, show

class MyBinaryTreeNode(Node):
	def __init__(self,value):
		self.value = value
		self.parent = None
		self.left = None
		self.right = None

	def add(self,new_node):
		if new_node.value >= self.value:
			if self.right is None:
				self.right = new_node
				new_node.parent = self
			else:
				self.right.add(new_node)
		else:
			if self.left is None:
				self.left = new_node
				new_node.parent = self
			else:
				self.left.add(new_node)

    def exists(self,value_to_search_for):
    if self.value == value_to_search_for:
        return True
    else:
        if value_to_search_for > self.value:
            # go to the right
            if self.right == None:
                # end of tree
                return False
            else:
                return self.right.exists(value_to_search_for)
        else:
            # go to the left
            if self.left == None:
                return False
            else: 
                return self.left.exists(value_to_search_for)



class BST:
	def __init__(self):
		self.root = None

	def add(self,value):
		new_node = MyBinaryTreeNode(value)

		if self.root is None:
			self.root = new_node
		else:	
			self.root.add(new_node)

	def exists(self,value):
		# return true if the value exists in the tree
		# return false if its doesn't exist in the tree
		if self.root is None:
			return False
		else:
			return self.root.exists(value)

def random_numbers(total_numbers):
    return [int(1000 * nprnd.random()) for i in range(total_numbers)]



tree = BST()
a = random_numbers(10)
for i in a:
	tree.add(i)


show(tree.root)
print tree.exists(a[9])


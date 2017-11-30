# most commonly used data structure for mysql
# a tree is a set of nodes where there is one path from the root to any other children
# root is the only way to access any other nodes in the tree
# ever node can only have one parent(thats why it only has one path)
# leaves-nodes without children
# subtree--any part of the tree that has a height greater than one
# depth--the level that a certain node is on (distance from the root)
# a tree has pointers to its chidl and its parent

class MyTreeNode:
	def __init__(self,value):
		self.value = value
		self.parent = None
		self.children = []
		# the array is the children

	def add_child(self,child_node):
		self.children.append(child_node)
		child_node.parent = self

	def remove_child(self, child_node):
		del self.children[self.children.indexof(child_node)]

root = MyTreeNode(5)
root.add_child(MyTreeNode(10))
root.add_child(MyTreeNode(20))

for child in root.children:
	print child.value





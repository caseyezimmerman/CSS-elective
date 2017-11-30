class LinkedListNode:
	def __init__(self, value):
		self.value = value
		self.right = None
		self.left = None

class LinkedList:
	def __init__(self):
		self.start = None
		self.end = None

	def append(self, value):
		new_node = LinkedListNode(value)

		if self.start is None:
			self.start = new_node
			self.end = new_node
		else:
			self.end.right = new_node
			new_node.left = self.end
			self.end = new_node

	def search(self,value):
		# is current.value = target? if yes return true, we found it
		# if not...we reassign current to the next node in the list. current.next
		current_node = self.start

		while current_node is not None:
			# if current_node.value == value:
			# 	return current_node
			print(current_node.value)
			current_node = current_node.right

linked_list = LinkedList()

for i in range(100):
	linked_list.append(i)

result = linked_list.search(50)

if result is not None:
	print result.value
else:
	print "Value not found"



a = LinkedListNode(10)
b = LinkedListNode(15)

a.right = b
b.left = a
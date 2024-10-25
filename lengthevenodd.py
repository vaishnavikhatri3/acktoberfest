# Python program to check length 
# of a given linklist 
# Defining structure 
class Node: 
	def __init__(self, d):
		self.data = d
		self.next = None
		self.head = None

	# Function to check the length 
	# of linklist 
	def LinkedListLength(self):
		while (self.head != None and
			self.head.next != None): 
			self.head = self.head.next.next
			
		if(self.head == None):
			return 0
		return 1
	
	# Push function 
	def push(self, info):
		
	# Allocating node 
		node = Node(info) 

	# Next of new node to head 
		node.next = (self.head) 

	# head points to new node 
		(self.head) = node 

# Driver code 
head = Node(0) 
	
# Adding elements to Linked List 
head.push(4) 
head.push(5) 
head.push(7) 
head.push(2) 
head.push(9) 
head.push(6) 
head.push(1) 
head.push(2) 
head.push(0) 
head.push(5) 
head.push(5) 
check = head.LinkedListLength()
	
# Checking for length of 
# linklist 
if(check == 0):
	print("Even")
else:
	print("Odd")
# This code is contributed by Prerna saini

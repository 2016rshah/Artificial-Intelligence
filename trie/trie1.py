class Node(object):
	def __init__(self, value):
		self.value = value
		self.children = {}
	def insert(stng = "cat"):
		if(len(stng) > 0):
			if(stng[0] in self.children):
				self.children[stng[0]].insert(stng[1:])
			elif(stng[0] not in self.children):
				p = Node(stng[0])
				self.children[p.value] = p
				p.insert(stng[1:])
		else:
			p = Node("$")
			self.children[p.value] = p

def main():
	root = Node("*")
	root.insert("cat")
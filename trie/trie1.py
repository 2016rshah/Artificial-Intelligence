class Node(object):
	def __init__(self, value):
		self.value = value
		self.children = {}
	def insert(self, stng = "cat"):
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
	def display(self):
		if self.value == '$': return 
		print('=========NODE=======')
		print('--> self.value	=',self.value)
		print('--> self.children: [',end = '')
		for key in self.children:
			if key != '$':
				print(key, sep = '', end = ', ')
		print(']')
		print("===================")
	def printWords(self, stng=""):
		for child in self.children:
			if(child == '$'):
				print(stng)
			else:
				tempStng = stng+self.children[child].value
				self.children[child].printWords(tempStng)
	def search(self, stng):
		pass #do this lol not gonna do it now
		node = self
		for i in range(len(stng)):
			if(stng[i] in node.children):
				node = node.children[stng[i]]
			else:
				return False
		if('$' in node.children):
			return True
		else:
			return False

def main():
	root = Node("*")
	root.insert("cat")
	root.insert("catnip")
	root.insert("cats")
	root.insert("catnap")
	root.insert("can't")
	root.insert("cat-x")
	root.insert("dog")
	root.insert("dognip")
	root.insert("")
	root.printWords()
	searchWord = input("Word to search for: ")
	if(root.search(searchWord)):
		print(searchWord, "is in the trie")
	else:
		print(searchWord, "is not in the trie")
main()
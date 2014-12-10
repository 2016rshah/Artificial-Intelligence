from random import choice
class Node(object):
	def __init__(self, value):
		self.value = value
		self.children = {}
	def __repr__(self):
		self.printNodes()
		return ''
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
	def printNodes(self, stng=""):
		if(self.value == '$'):
			print(stng[1:])
		else:
			for child in self.children:
				#print(child)
				self.children[child].printNodes(stng+self.value)
	def randomChild(self):
		return choice(list(self.children))
	def searchForNextLetter(self, stng):
		node = self
		for i in range(len(stng)):
			node = node.children[stng[i]]
		return node.randomChild()
	def fragmentInDictionary(self, stng):
		node = self
		for i in range(len(stng)):
			if(stng[i] in node.children):
				node = node.children[stng[i]]
			else:
				return False
		return True
	def spellWordFromString(self, stng):
		x = self.searchForNextLetter(stng)
		while(x != '$'):
			stng+=x
			x = self.searchForNextLetter(stng)
		return stng



from sys import setrecursionlimit; setrecursionlimit(100)
from time import clock

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
	#print(root)
	root.printNodes()
	print("SEARCH:", root.search('*'))
	printElapsedTime()
	#root.printWords()
	# searchWord = input("Word to search for: ")
	# if(root.search(searchWord)):
	# 	print(searchWord, "is in the trie")
	# else:
	# 	print(searchWord, "is not in the trie")
def printElapsedTime():
	print('\n--Total run time =', round(clock()-startTime, 2),'seconds.')

# if __name__ == '__main__':
# 	startTime = clock()
# 	main()
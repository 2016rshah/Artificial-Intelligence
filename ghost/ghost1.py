from Trie import Node

def printGhostDirections():
	print('+----------------------------+')
	print('|Welcome to the game of GHOST|')
	print('|The human goes first. Enter |')
	print('|your letters in the pop-up  |')
	print('|dialog boxes. Good luck!    |')
	print('+----------------------------+')
def createTrieFromDictionaryFile():
	root = Node("*")
	file1 = open("words.txt")
	for word in file1:
		root.insert(word.lower().strip())
	file1.close()
	return root
def requestAndCheckHumanMove(root, stng):
	stng += input("HUMAN, enter your character.").lower()[0]
	print(' ', stng)
	if(root.search(stng)):
		print("-"*50)
		print('HUMAN LOSES because"', stng, '" is a word.', sep = '')
		print('-'*19, "<GAME OVER>", '-'*18)
		exit()
	if not root.fragmentInDictionary(stng):
		print("-"*50)
		print('HUMAN LOSES because "', stng, '" does not begin any words.', sep = '')
		print("[The computer's word was ", root.spellWordFromString(stng[0:-1]), "]", sep="")
		print('-'*18, "<GAME OVER>", '-'*18)
		exit()
	return stng


def main():
	root = createTrieFromDictionaryFile()
	printGhostDirections()
	stng = '' #current string
	while True:
		stng = requestAndCheckHumanMove(root, stng)
		#stng = requestAndCheckComputerMove(root, stng)
	
main()
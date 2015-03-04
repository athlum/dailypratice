#-*- coding:utf-8 -*-
'''
AC自动机

http://www.cnblogs.com/huangxincheng/archive/2012/12/02/2798317.html
'''

from utils import print_cost

class TreeNode:
	def __init__(self,word='',isroot=False):
		self.childNodes = {}
		self.isfinal = False
		self.nodeChar = word
		self.failNode = None
		self.isroot = isroot
		self.id = None
		self.wordcontext = None


class TrieTree:
	def __init__(self,wordlist=''):
		self.treeNode = TreeNode(isroot=True)
		if wordlist:
			self.CreatrTrieTree(wordlist)

	def AddTrieNode(self,words,wid,wordcontext,currentNode=None):
		if not words:
			return

		if not currentNode:
			currentNode = self.treeNode

		word = words[0]

		if not currentNode.childNodes.get(word,None):
			currentNode.childNodes[word] = TreeNode(word=word)

		words = words[1:]

		if not words:
			currentNode.childNodes[word].isfinal = True
			currentNode.childNodes[word].id = wid
			currentNode.childNodes[word].wordcontext = wordcontext

		self.AddTrieNode(words,wid,wordcontext,currentNode.childNodes[word])

	def BuildFailNode(self,currentNode=None):
		if not currentNode:
			currentNode = self.treeNode
		# 	print 'root',None,currentNode.isroot,currentNode.isfinal
		# else:
		# 	print currentNode.nodeChar,currentNode.failNode.nodeChar,currentNode.isroot,currentNode.isfinal

		for node in currentNode.childNodes.values():
			if currentNode.isroot:
				node.failNode = self.treeNode
			else:
				failNode = currentNode.failNode

				while failNode:
					if failNode.childNodes.get(node.nodeChar,None):
						node.failNode = failNode.childNodes[node.nodeChar]
						break

					failNode = failNode.failNode

				if not failNode:
					node.failNode = self.treeNode

			self.BuildFailNode(currentNode=node)

	@print_cost
	def CreatrTrieTree(self,wordlist):
		for index in range(len(wordlist)):
			self.AddTrieNode(wordlist[index],index,wordlist[index])

		self.BuildFailNode()

	@print_cost
	def Search(self,context):
		result = []
		currentNode = self.treeNode
		for index in range(len(context)):
			word = context[index]
			# print 'currentNode',currentNode.nodeChar,word
			node = None
			while currentNode:
				node = currentNode.childNodes.get(word,None)
				if node:
					# print 'node',node.nodeChar
					if node.isfinal:
						result.append({'index':index+1-len(node.wordcontext),'id':node.id})
					else:
						currentNode = node
						break
				if not node or node.isfinal:
					failNode = currentNode.failNode
					if failNode:
						currentNode = failNode
					else:
						currentNode = self.treeNode
						break

		return result
				

if __name__ == '__main__':
	wordlist = ['abcde','abfg','hijkl','cdef']

	tree = TrieTree(wordlist)
	print tree.Search('abcfabcdefghijklabhijk')
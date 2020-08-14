"""
Given an array of strings, find if the given strings can be chained to form a circle. A string X can be put before another string Y in circle if the last character of X is same as first character of Y.

In des
First line contain integer N,size of array.
Second line contain N space separated strings,denotes strings in array.

Ot des
Print yes or no

2
geek king

Exp
From sample
Yes, the given strings can be chained.
Note that the last character of first string is same
as first character of second string and vice versa is
also true.

Hint
Find if the ending and starting char of string equal,and the last strings last char should be equal to first strings first char.

H-7
T-1500


""" 
CHARS = 26
class Graph(object): 
	def __init__(self, V): 
		self.V = V
		self.adj = [[] for x in xrange(V)] 
		self.inp = [0] * V 
	def addEdge(self, v, w): 
		self.adj[v].append(w) 
		self.inp[w]+=1 
	def isSC(self): 
 
		visited = [False] * self.V  
		n = 0
		for n in xrange(self.V): 
			if len(self.adj[n]) > 0: 
				break
		self.DFSUtil(n, visited) 
		for i in xrange(self.V): 
			if len(self.adj[i]) > 0 and visited[i] == False: 
				return False
		gr = self.getTranspose() 
		for i in xrange(self.V): 
			visited[i] = False
		gr.DFSUtil(n, visited)  
		for i in xrange(self.V): 
			if len(self.adj[i]) > 0 and visited[i] == False: 
				return False

		return True

	def isEulerianCycle(self):  
		if self.isSC() == False: 
			return False 
		for i in xrange(self.V): 
			if len(self.adj[i]) != self.inp[i]: 
				return False

		return True
	def DFSUtil(self, v, visited): 
		visited[v] = True
		for i in xrange(len(self.adj[v])): 
			if not visited[self.adj[v][i]]: 
				self.DFSUtil(self.adj[v][i], visited)  
	def getTranspose(self): 
		g = Graph(self.V) 
		for v in xrange(self.V):  
			for i in xrange(len(self.adj[v])): 
				g.adj[self.adj[v][i]].append(v) 
				g.inp[v]+=1
		return g 
def canBeChained(arr, n): 
	g = Graph(CHARS)  
	for i in xrange(n): 
		s = arr[i] 
		g.addEdge(ord(s[0])-ord('a'), ord(s[len(s)-1])-ord('a')) 
	return g.isEulerianCycle()  
N=int(input())
arr1 = list(map(int,input().split())
n1 = len(arr1) 
if canBeChained(arr1, n1): 
	print("yes")
else: 
	print("no")



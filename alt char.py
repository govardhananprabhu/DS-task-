"""
Given a string of both uppercase and lowercase alphabets, the task is to print the string with alternate occurrences of any character dropped(including space and consider upper and lowercase as same).

String len <= 50
H 6 T 2000
Tag string

In des
First line contains only one sentence.

Ot des
Print the altered sentence

It is a long day Dear.
It sa longdy ear.

guvi geek network
guvi eknetwor

codekatta platform
codekat platfrm

webkatta platform
webkat platform

python
python

Exp
Print first I and then ignore next i.
Similarly print first space then 
ignore next space.

Hint
As we have to print characters in alternate manner, so start traversing the string and perform following two steps:-
Increment the count of occurrence of current character in a hash table.
Check if the count becomes odd, then print the current character, else not.

"""
def printStringAlternate(string): 

	occ = {} 

	for i in range(0, len(string)): 
		temp = string[i].lower() 
		occ[temp] = occ.get(temp, 0) + 1
		if occ[temp] & 1: 
			print(string[i], end = "") 

	print()
str=input()
printStringAlternate(str) 



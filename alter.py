"""
Question
Given a string of both uppercase and lowercase alphabets, the task is to print the
string with alternate occurrences of any character dropped(including space and consider
upper and lowercase as same)

Input description
First line has string

Output description
print the modified string

Explanation
Input : It is a long day Dear.
Output : It sa longdy ear.
Print first I and then ignore next i.
Similarly print first space then 
ignore next space.

Input
It is a long day Dear.
Output
ItisalongdayDear.
Input
the master
Output
the masr
Input
butter milk chocolate
Output
buter milkchoat
Input
tata
Output
ta
Input
e
Output
e
Hint
As we have to print characters in alternate manner, so start traversing the string and perform following two steps:-

Increment the count of occurrence of current character in a hash table.
Check if the count becomes odd, then print the current character, else not.
Solution:"""
def printStringAlternate(string): 

	occ = {} 
 
	for i in range(0, len(string)): 
		temp = string[i].lower() 
		occ[temp] = occ.get(temp, 0) + 1

		if occ[temp] & 1: 
			print(string[i], end = "") 

	print() 
if __name__ == "__main__": 

	string = input()
	printStringAlternate(string) 



"""
Print all possible words from phone digits
Note:
Before the advent of QWERTY keyboards, texts and numbers were placed on the same key. For example, 2 has “ABC” if we wanted to write anything starting with ‘A’ we need to type key 2 once. If we wanted to type ‘B’, press key 2 twice and thrice for typing ‘C’. Below is a picture of such keypad.

H 7
T 3000
Tag accolite,string.
In des
First line contain integer N.

Ot des
Print the count of all possible words can be typed.

234
27

2
3

27
12

23
9

5
3

Exp
From sample:
All possible words which can be 
formed are (Alphabetical order):
adg adh adi aeg aeh aei afg afh 
afi bdg bdh bdi beg beh bei bfg 
bfh bfi cdg cdh cdi ceg ceh cei 
cfg cfh cfi
If 2 is pressed then the alphabet
can be a, b, c, 
Similarly, for 3, it can be 
d, e, f, and for 4 can be g, h, i.

Hint
Create a hash map which has all the integer's word,from the input given find the count of possible words typed.

"""
hashTable = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"] 

def printWordsUtil(number, curr, output, n):
    if(curr == n):
        ans.append(output)
        return
    for i in range(len(hashTable[number[curr]])):
        output.append(hashTable[number[curr]][i])
        printWordsUtil(number, curr + 1, output, n)
        output.pop()
        if(number[curr] == 0 or number[curr] == 1):
            return; 
 
def printWords(number, n):
	printWordsUtil(number, 0, [], n)  
N=input()
number=[]
ans=[]
for i in N:
    number.append(int(i)) 
n = len(number)
printWords(number, n)
print(len(ans))

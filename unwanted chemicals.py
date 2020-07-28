"""
Question
Docter strange needs to find a cure for hulk,he has two string he need to remove the
missmatch character from two strings,then he can mix the two array to find cure,print
the missmatch,else -1.

Input description
First line has string 1
Second line has string 2

Output description
print missmatch char or -1

Explanation
Input: str1 = “characters”, str2 = “alphabets”
Output: b c l p r


Input
water
bater
Output
b w

Input
eeeet
wrtree
Output
r w

Input
master
teacher
Output
c h m s

Input
foreign
abroad
Output
a b d e f g i n

Input
abcd
dcba
Output
-1

Hint
Using two loops, for each character of 1st string check whether it is present in the 2nd string or not. Likewise, for each character of 2nd string check whether it is present in the 1st string or not.
Soution"""
MAX_CHAR = 26
def findAndPrintUncommonChars(str1, str2): 

	present = [0] * MAX_CHAR 
	for i in range(0, MAX_CHAR): 
		present[i] = 0

	l1 = len(str1) 
	l2 = len(str2) 

	for i in range(0, l1): 
		present[ord(str1[i]) - ord('a')] = 1
	for i in range(0, l2): 
		if(present[ord(str2[i]) - ord('a')] == 1 or
		present[ord(str2[i]) - ord('a')] == -1): 
			present[ord(str2[i]) - ord('a')] = -1

		else: 
			present[ord(str2[i]) - ord('a')] = 2

	for i in range(0, MAX_CHAR): 
		if(present[i] == 1 or present[i] == 2): 
			ans.append(chr(i + ord('a')))
	
if __name__ == "__main__": 
	str1 = input()
	str2 = input()
	ans=[]
	findAndPrintUncommonChars(str1, str2) 
if(len(ans)==0):
    print(-1)
else:
    print(*ans)

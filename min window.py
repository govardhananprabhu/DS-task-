"""
You are given with two strings find the Smallest window in a string containing all
characters of another string.If not print "No such window exists".

Input description
First line has two integers contains the size of two strings
SEcond line has main string
Third line has the string which is to be founded in first
Output description
print the window

Explanation
Input: string = “this is a test string”, pattern = “tist”
Output: Minimum window is “t stri”
Explanation: “t stri” contains all the characters of pattern.

Input
21 4
this is a test string
tist
Output
t stri

Input
13 3
geeksforgeeks
ork
Output
ksfor

Input
3 1
wat
e
Output
No such window exists


"""
no_of_chars = 256

def findSubString(string, pat): 

	len1 = len(string) 
	len2 = len(pat)
	print(len1,len2)
	if len1 < len2: 
	
		print("No such window exists") 
		return "" 

	hash_pat = [0] * no_of_chars 
	hash_str = [0] * no_of_chars 
	for i in range(0, len2): 
		hash_pat[ord(pat[i])] += 1

	start, start_index, min_len = 0, -1, float('inf') 
	count = 0 
	for j in range(0, len1): 
		hash_str[ord(string[j])] += 1
		if (hash_pat[ord(string[j])] != 0 and
			hash_str[ord(string[j])] <=
			hash_pat[ord(string[j])]): 
			count += 1

		if count == len2: 
			while (hash_str[ord(string[start])] > 
				hash_pat[ord(string[start])] or
				hash_pat[ord(string[start])] == 0): 
			
				if (hash_str[ord(string[start])] > 
					hash_pat[ord(string[start])]): 
					hash_str[ord(string[start])] -= 1
				start += 1
			
	    
			len_window = j - start + 1
			if min_len > len_window: 
			
				min_len = len_window 
				start_index = start 
	if start_index == -1: 
		print("No such window exists") 
		return "" 
	
	return string[start_index : start_index + min_len] 
N,M=map(int,input().split())
string = input()
pat = input()
print(findSubString(string, pat)) 
	

"""
Given two strings, find the number of times the second string occurs in the first string, whether continuous or discontinuous.
Note string length<=25

H 6 T 2300
Tag accolite string

In des
First line and second line contains a single string s1,s2.

Ot des
Print the count

Examples:
guvigeek
gk
2

guviplatform
gfm
1

guvigeekguvi
gk
2

codekattacrackers
crs
5

hiring
hn
1

Explanation:  
The four strings are - (Check characters marked in "")
"g"uvigee"k"
guvi"g"ee"k"


Hint
The idea is to process all characters of both strings one by one staring from either from left or right side. Let us traverse from right corner, there are two possibilities for every pair of character being traversed.

"""
def count(a, b, m, n):  
	if ((m == 0 and n == 0) or n == 0): 
		return 1
	if (m == 0): 
		return 0 
	if (a[m - 1] == b[n - 1]): 
		return (count(a, b, m - 1, n - 1) +
				count(a, b, m - 1, n)) 
	else: 
		return count(a, b, m - 1, n) 

a = input()
b = input()

print(count(a, b, len(a),len(b))) 



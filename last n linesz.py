"""
Given some text lines in one string, each line is separated by ‘\n’ character. Print the last N lines. If the number of lines is less than N, then print all lines.
given string ="str1\nstr2\nstr3\nstr4\nstr5\nstr6" + \ 
         "\nstr7\nstr8\nstr9\nstr10\nstr11" + \ 
         "\nstr12\nstr13\nstr14\nstr15\nstr16" + \ 
         "\nstr17\nstr18\nstr19\nstr20\nstr21" + \ 
         "\nstr22\nstr23\nstr24\nstr25"
H 5 T 1500
Tag string

In des
First line contains single integer denotes number of lines to print.

Ot des
Print the every string in each line till n. 

5
str21
str22
str23
str24
str25

Exp
the last 5 strings are
str21
str22
str23
str24
str25

25
str1
str2
str3
str4
str5
str6
str7
str8
str9
str10
str11
str12
str13
str14
str15
str16
str17
str18
str19
str20
str21
str22
str23
str24
str25

2
str24
str25

4
str22
str23
str24
str25

1
str25
Hint
From the given string print the last n strings in each line.
"""
def PrintLast(s, t): 
	v = s.split('\n') 
	
	if len(v) == 0: 
		print("ERROR") 
		return
	elif len(v) >= t: 
		for i in range(len(v) - t, len(v)): 
			print(v[i]) 
	
	else: 
		for i in range(0, len(v)): 
			print(v[i]) 
if __name__ == "__main__": 

	s1 = "str1\nstr2\nstr3\nstr4\nstr5\nstr6\nstr7\nstr8\nstr9\nstr10\nstr11\nstr12\nstr13\nstr14\nstr15\nstr16\nstr17\nstr18\nstr19\nstr20\nstr21\nstr22\nstr23\nstr24\nstr25"
	
	n = int(input())
	PrintLast(s1, n) 

"""
Given two times in string “HH:MM” format. Here ‘H’ shows hours and ‘M’ shows minutes. You have to find the difference in the same string format between these two strings. But both given strings should follow these cases.
1) Time 1 will be less than or equal to time2
2) Hours will be possible from 0 to 23.
3) Minutes will be possible from 0 to 59

H 6
t 2000
Tag accolite

In des
First line contains a space separated 2 strings,which denotes times.

Ot des
print the difference


14:00 16:45

2:45

1:04 13:05

12:01

1:00 1:00

0:0

12:23 22:50

10:27

11:00 23:22

12:22

Exp
From sample:
the difference is 14:00-16:45 = 2:45

Hint
The idea is to first remove colon. After removing colon, hour difference can be computed using simple mathematics.

"""
def removeColon(s): 
	
	if (len(s) == 4): 
		s = s[:1] + s[2:] 
	
	if (len(s) == 5): 
		s = s[:2] + s[3:] 
	
	return int(s)  
def diff(s1, s2): 
	time1 = removeColon(s1) 
	time2 = removeColon(s2)  
	hourDiff = time2 // 100 - time1 // 100 - 1;  
	minDiff = time2 % 100 + (60 - time1 % 100) 

	if (minDiff >= 60): 
		hourDiff += 1
		minDiff = minDiff - 60 
	res = str(hourDiff) + ':' + str(minDiff) 
	
	return res 
s1,s2=input().split()

print(diff(s1, s2)) 



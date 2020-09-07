"""
Given a number n, find the greatest number that has same set of digits as n. If n is the greatest possible number with its set of digits, then print “-1”.
T 2100
H 6
Tag Yahoo string

In des
First line contains integer N.
Ot des
Print the next gretaer integer.

218765
251678

1234
1243

4321
-1

534976
536479

123
132

Exp
For example, if the input number is “534976”, we stop at 4 because 4 is smaller than next digit 9. If we do not find such a digit, then output is “-1”.
Hint
Traverse the given number from rightmost digit, keep traversing till you find a digit which is smaller than the previously traversed digit.

""" 
def findNext(number,n): 
	for i in range(n-1,0,-1): 
		if number[i] > number[i-1]: 
			break
	if i == 1 and number[i] <= number[i-1]: 
		print(-1)
		return 
	x = number[i-1] 
	smallest = i 
	for j in range(i+1,n): 
		if number[j] > x and number[j] < number[smallest]: 
			smallest = j 
	number[smallest],number[i-1] = number[i-1], number[smallest] 
	x = 0 
	for j in range(i): 
		x = x * 10 + number[j] 
	number = sorted(number[i:]) 
	for j in range(n-i): 
		x = x * 10 + number[j] 
	
	print(x) 

digits = input()		
number = []
for i in digits:
    number.append(int(i))
findNext(number, len(digits)) 

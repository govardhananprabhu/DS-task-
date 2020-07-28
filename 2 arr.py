"""
Question
Scientist had almost founded the antidot of virus,they need to make two solutions value
same,the two solutions are arrays with integer,the scientist shuold balance the
two array by swapping oone element from each array,print the two element else -1 -1.

Input description
First ine has list of integer
Second line has list of integer

Output description
print the two integer value

Explanation
Input: A[] = {4, 1, 2, 1, 1, 2}, B[] = (3, 6, 3, 3)
Output: {1, 3}
Sum of elements in A[] = 11
Sum of elements in B[] = 15
To get same sum from both arrays, we
can swap following values:
1 from A[] and 3 from B[]

Input
2 3 4 5 6
2 3 4 5 6
Output
2 2

Input
1 2 3 4 5 6
7 8 9 10 1 2 1 1 1 1 1 1
Output
-1 -1

Input
1 1 1 1 1 1 1 1 1 1
1 10
Output
-1 -1

Input
1 1 1 1 1 1 1 1 1
1 9
Output
-1 -1

Input
1 1 1 1 1 1 1 1 1 1
1 9
Output
1 1

Hint
Iterate through the arrays and check all pairs of values. Compare new sums or look for a pair with that difference.

Solution:"""
def getSum(X): 
	sum=0
	for i in X: 
		sum+=i 
	return sum
def findSwapValues(A,B): 
	sum1=getSum(A) 
	sum2=getSum(B) 


	k=False


	val1,val2=-1,-1
	for i in A: 
		for j in B: 
			newsum1=sum1-i+j 
			newsum2=sum2-j+i 
			
			if newsum1 ==newsum2: 
				val1=i 
				val2=j
				k=True
				break
		 
		if k==True: 
			break
	print(val1,val2) 
	return



A=list(map(int,input().split()))
B=list(map(int,input().split()))



findSwapValues(A,B) 


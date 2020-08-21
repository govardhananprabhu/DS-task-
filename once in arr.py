"""
Given a sorted array in which all elements appear twice (one after one) and one element appears only once. Find that element in O(log n) complexity.



In des
First line contain integers N, denotes size of array.
Second lines contain N space separated integers,denotes array elements.

Ot des
Print the element,if no element present once print "Invalid Array".
11
1 1 3 3 4 5 5 7 7 8 8

4

11
1 1 3 3 4 4 5 5 7 7 8

8
Exp
From sample
Element 4 is present only once in given array. 

Hint
A Simple Solution is to traverse the array from left to right. Since the array is sorted, we can easily figure out the required element.

H 6

T 2000

"""
N=int(input())
L=list(map(int,input().split()))
for i in range(N):
    if(L.count(L[i])==1):
        print(L[i])
        break
    if(i==N-1):
        print("Invalid Array")
        break
    


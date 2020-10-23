"""
There is an array contains N number of patients in hospital ,the task is to find the Kth weakest person in it. 

H 4 T cisco
T 1000

In des
First line contains integer N,denotes size of array.
Second line contains N space separated integers ,denotes array elements.
Third line contains integer K ,denotes kth person.

Ot
Print the Kth weakest person.

Exp
7 is the 3rd weakest person in hospital

6
7 10 4 3 20 15
3
7

6
7 10 4 3 20 15
4
10

4
2 1 4 3
2
2

7
12 44 135 45 1121 1789 76
4
76

6
7 10 4 3 20 15
6
3

Hint
Sort the array and print the Kth element of array from end.

"""
N=int(input())
arr = list(map(int,input().split()))
k = int(input())
arr.sort()
print(arr[-1*k])

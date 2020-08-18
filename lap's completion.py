"""
There are some atheletes running in circular ground,you to find the number of laps completed by each atheletes.You are given with array of integers,which are atheletes,the lap count is equal to count of elements in it.

In des
First line contain integer N,denotes size of array.
Second line contain N space separated integers,denotes athelets.

Ot des
Print the space separated count of each atheletes.

5
1 2 1 2 3 

2 2 1

Exp
From sample
1 and 2 completed 2 laps,3 completed only 1.

Hint
Traverse the array and find the count of each element in arr.

H 4
T 2000


"""
N=int(input())
arr = list(map(int,input().split()))
ans=[]
res=[]
for i in arr:
    if i not in ans:
        ans.append(i)
        res.append(arr.count(i))
print(*res)

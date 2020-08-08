"""
Given an integer array of size N,the integers in array are the quantity of milk with chocolate
and a positive integer k is the correct amount, count all distinct milk with chocolate pairs with
difference equal to k.



Exp
From sample
There are 2 pairs with difference 3, the pairs are {1, 4} and {5, 2}

Hin
A simple solution is to consider all pairs one by one and check difference
between every pair

I
5
1 5 3 4 2
3
O
2


I
6
1 2 3 5 6 7
5
O
2


I
6
1 2 3 4 5 6
1
O
5

I
1
1
1
O
0

I
3
8 7 4
3
O
1

T 1400

"""
def countPairsWithDiffK(arr, n, k): 
    count = 0
    for i in range(0, n):
        for j in range(i+1, n) : 
              
            if arr[i] - arr[j] == k or arr[j] - arr[i] == k: 
                count += 1
                  
    return count 
  
N=int(input())
arr = list(map(int,input().split()))
  
n = len(arr) 
k = int(input())
print (countPairsWithDiffK(arr, n, k)) 

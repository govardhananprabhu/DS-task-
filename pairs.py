"""
Given an array of integers and a number k, write a function that returns true if given array can be divided into pairs such that sum of every pair is divisible by k.

In des
First line contain integer N,denotes size of array.
Second line contain N space separated integers,denotes array elements.

Ot des
Print yes or no

4
9 7 5 3
6
yes

6
92 75 65 48 45 35
10
yes

4
91 74 66 48
10
no

Exp
From sample
We can divide array into (9, 3) and
(7, 5). Sum of both of these pairs
is a multiple of 6.

Hint
A Simple Solution is to iterate through every element arr[i]. Find if there is another not yet visited element that has remainder as (k – arr[i]%k). If there is no such element, return false. If a pair is found, then mark both elements as visited.

H 6
T 2400

"""
#include <bits/stdc++.h> 
using namespace std; 
bool canPairs(int arr[], int n, int k) 
{ 
	if (n & 1) 
		return false; 
	unordered_map<int, int> freq; 
	for (int i = 0; i < n; i++) 
		freq[arr[i] % k]++; 
	for (int i = 0; i < n; i++) 
	{ 
		int rem = arr[i] % k; 
		if (2*rem == k) 
		{ 
			if (freq[rem] % 2 != 0) 
				return false; 
		} 

		else if (rem == 0) 
		{ 
		if (freq[rem] & 1)		 
			return false; 
		}		 

		else if (freq[rem] != freq[k - rem]) 
			return false; 
	} 
	return true; 
} 

int main() 
{ 
	int N;
	cin >> N;
	int arr[N];
	for (int i = 0; i < N; ++i){
    cin >> arr[i];
	    
	}
	int k;
	cin >> k;
	int n = sizeof(arr)/sizeof(arr[0]); 
	canPairs(arr, n, k)? cout << "yes": cout << "no"; 
	return 0; 
}


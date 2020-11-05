"""
Calculate difficulty of a given sentence. Here a Word is considered hard if it has 4 consecutive consonants or number of consonants are more than number of vowels. Else word is easy. Difficulty of sentence is defined as 5*(number of hard words) + 3*(number of easy words).

string len <= 50

H 5 T 1500
Tag string

In des
First line contains string only.

Ot des
Print the difficulty value.

Difficulty of sentence

13

guvi geek network

11

codekatta

5

webkatta

5

java

3


Exp
Hard words = 2(Difficulty and sentence)
Easy words = 1(of)
So, answer is 5*2+3*1 = 13

Hint
Increment vowels count, if current character is vowel and set conecutive consonants count=0.
Else increment consonants count, also increment consecutive consonants count.
Check if consecutive consonants becomes 4, then current word is hard, so increment its count
and move to the next word.Reset all counts to 0.
Else check if a word is completed and count of consonants is greater than count of vowels,
then it is a hard word else easy word.Reset all counts to 0.

"""
def isVowel(ch): 
	return (ch == 'a'  or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u') 
def calcDiff(str): 
	str = str.lower() 
	count_vowels = 0
	count_conso = 0
	consec_conso = 0
	hard_words = 0
	easy_words = 0
	for i in range(0, len(str)): 
		if(str[i]!= " " and isVowel(str[i])):  
			count_vowels += 1
			consec_conso = 0 
		elif(str[i] != " "): 
			count_conso += 1
			consec_conso += 1
		if(consec_conso == 4): 
			hrad_words += 1 
			while(i < len(str) and str[i] != " "): 
				i += 1
			count_conso = 0
			count_vowels = 0
			consec_conso = 0
		elif(i < len(str) and (str[i] == ' ' or
						i == len(str) - 1)): 
			if(count_conso > count_vowels): 
				hard_words += 1
			else: 
				easy_words += 1
			count_conso = 0
			count_vowels = 0
			consec_conso = 0 
	return (5 * hard_words + 3 * easy_words) 
	
str = input()
print(calcDiff(str)) 


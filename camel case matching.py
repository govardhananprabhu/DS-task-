"""
Given a dictionary of words where each word follows CamelCase notation, print all words in the dictionary that match with a given pattern consisting of uppercase characters only.

T 2500
H 6
Tag dict,olacabs,string.

In des
First line contains an integer n denoting the number of words in the dictionary.
The next line contains the vector of strings in the dictionary.
The last line contains the pattern.

Ot des
Print all words in the dictionary that match with a given pattern consisting of uppercase characters only in single line space separated. If the pattern is not found, print "No match found" (without quotes).

8
Hi Hello HelloWorld HiTech HiGeek HiTechWorld HiTechCity HiTechLab
HA

No match found

3
WelcomeGuvi WelcomeToCodekata Code
WTC

WelcomeToCodekata

3
WelcomeGuvi WelcomeToCodekata WaterGost
WG
WelcomeGuvi WaterGost

3
TapTok TikTok TickTack
TT
TapTok TikTok TickTack

4
MapG PubG FagG FiveG
PG

PubG

Exp
There is only one abbreviation for the given pattern i.e., WelcomeToCodekata.

Traverse through every word and keep Hashing that word with every uppercase letter found in the given string.
After creating hashing for all the string in the list. Search for the given pattern in the map and print all the string mapped to it.
"""
def CamelCase(words, pattern) :  
	map = dict.fromkeys(words,None); 
	for i in range(len(words)) : 
		string = ""; 
		l = len(words[i]); 
		for j in range(l) : 
			if (words[i][j] >= 'A' and words[i][j] <= 'Z') : 
				string += words[i][j]; 
				
				if string not in map : 
					map[string] = [words[i]] 
					
				elif map[string] is None : 
					map[string] = [words[i]] 
					
				else : 
					map[string].append(words[i]); 

	wordFound = False; 
	for key,value in map.items() : 
		if (key == pattern) : 
			wordFound = True; 
			for itt in value : 
				print(itt,end=" "); 
	if (not wordFound) : 
		print("No match found"); 
 
N=int(input())
words = input().split()
pattern = input()
CamelCase(words, pattern); 

"""
Write a function to reverse a sentence.

H 4 T 1000
Tag cisco string

In des
First line contains a sentence strings only.

Ot des
Print the reverse

guvi quiz practice code 
code practice quiz guvi

getting good at coding needs a lot of practice 
practice of lot a needs coding at good getting 

i like this program very much
much very program this like i

codekatta ques
ques codekatta

a e v r s t
t s r v e a

Exp
Let the input string be “i like this program very much”. The function should change the string to “much very program this like i”

Hint
Reverse the whole string from start to end to get the desired output.
"""
def reverse_word(s, start, end):
	while start < end:
		s[start], s[end] = s[end], s[start]
		start = start + 1
		end -= 1


s = input()
s = list(s)
start = 0
while True:
	
	try:
		end = s.index(' ', start)
		reverse_word(s, start, end - 1)
		start = end + 1

	except ValueError:
		reverse_word(s, start, len(s) - 1)
		break
s.reverse()
s = "".join(s)
print(s)



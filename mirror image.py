"""
Manoj created a game which should contain mirror image of original string,the player needs to find the original string. 

In des
First line contain string,denotes mirror image.

Ot des
Print the original image.

jonaM
Manoj

Exp
From sample
Manoj is the mirror image of jonaM.
first char becomes last,and so on till the last becomes first. 
Hint
we call a function to reverse a string, which iterates to every element and intelligently join each character in the beginning so as to obtain the reversed string.

H 4
T 1300

"""  
def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
  
s = input()
print (reverse(s)) 

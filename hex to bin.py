"""
Question
Surya kept his savings in his locker but he forget the pin,he has a clue which is string.
It is in the form of hexadecimal value convert it into binary value.The bin value is
the pin.

Input description
single line string

Output description
binary value

Test Cases

Input
1AC5
Output
0001101011000101

Input
4444
Output
0100010001000100

Input
ABCD
Output
1010101111001101

Input
A2B9
Output
1010001010111001

Input
3546ADQ
Output
Invalid


Solution:"""
def to4DigitBin(value):  
	return '0'*(4-len(value))+value 

def HexadecimalToBinary(inputHexadecimal): 
	resultBinary = '' 

	for eachElement in inputHexadecimal:
		if(eachElement.isdigit()):
			binaryOfSingleDigit = bin(int(eachElement))[2:] 
			resultBinary += to4DigitBin(binaryOfSingleDigit)
		elif(eachElement.isalpha() and ord(eachElement) < 71): 
			resultBinary += to4DigitBin(bin(ord(eachElement)-55)[2:])  
		else:			 
			resultBinary = 'Invalid'
			break

	return resultBinary 
inputHexadecimal = input() 
print(HexadecimalToBinary(inputHexadecimal)) 

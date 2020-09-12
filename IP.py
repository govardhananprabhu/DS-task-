"""
Given an IP address as input, write a program to check whether the given IP Address is Valid or not.
Note:
Every computer connected to the Internet is identified by a unique four-part string, known as its Internet Protocol (IP) address. An IP address (version 4) consists of four numbers (each between 0 and 255) separated by periods. The format of an IP address is a 32-bit numeric address written as four decimal numbers (called octets) separated by periods; each number can be written as 0 to 255 (E.g. – 0.0.0.0 to 255.255.255.255).

H 5
Tag cisco string
T 2100

In des
First line contain string,which denotes IP address.

Ot des
Print Valid Ip address or Invalid Ip addess.

Input:  192.168.0.1
Output: Valid Ip address

Input: 110.234.52.124
Output: Valid Ip address

Input: 666.1.2.2
Output: Invalid Ip addess

122.123.223.333
Invalid Ip address

1.1.1.1
Valid Ip address

Exp
From sample:
all part's number is less than 256

Hint
We need to check every part's value is between 0 to 255
"""
import re 

regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
def check(Ip):
    if(re.search(regex, Ip)):
        print("Valid Ip address")
    else:
        print("Invalid Ip address")  

Ip = input()
check(Ip) 


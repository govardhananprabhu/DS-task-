"""
Given a string str, our task is to find the Largest Alphabetic Character, whose both uppercase and lowercase are present in the string. The uppercase character should be returned. If there is no such character then return -1 otherwise print the uppercase letter of the character.
H 4 T 1000
Tag string

In des
First line contains only one string.

Ot des
Print the largest alphabetic character.

admeDCAB
D

dAeB
-1

abcC
C

aA
A

wertT
T

Exp
Both the uppercase and lowercase characters for letter D is present in the string and it is also the largest alphabetical character, hence our output is D.

Hint
The naive method is to check for the presence of each character in the string for both uppercase or lowercase character that is for letter A both ‘a’ and ‘A’ should be there in the string. If such a letter is present then will keep track of that character and update only if the current character is greater than the previously chosen character.
"""
import java.util.*;  
public class Main {


	public static String largestCharacter(String str)
	{
		boolean[] uppercase = new boolean[26];
		boolean[] lowercase = new boolean[26];

		char[] arr = str.toCharArray();

		for (char c : arr) {

			if (Character.isLowerCase(c))
				lowercase = true;

			if (Character.isUpperCase(c))
				uppercase = true;
		}
		for (int i = 25; i >= 0; i--) {
			if (uppercase[i] && lowercase[i])
				return (char)(i + 'A') + "";
		}
		return "-1";
	}
	public static void main(String[] args)
	{
		Scanner sc= new Scanner(System.in); 
		String str= sc.nextLine(); 
		System.out.println(largestCharacter(str));
	}
}

#Write a program to input any alphabet and check whether it is vowel or consonant.

vowel = 'a','e','i','o','u','A','E','I','O','U'
alphabet = input("Enter a alphabet: ")

if alphabet in vowel:
    print('Alphabet is a  Vowel!')
else:
    print('Alphabet is a Consonant!')
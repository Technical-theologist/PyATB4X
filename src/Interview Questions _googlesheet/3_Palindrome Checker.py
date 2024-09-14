#Create a program that checks whether a given string is a palindrome.
# A palindrome is a word or phrase that reads the same backward as forward (ignoring spaces, punctuation, and capitalization).
# Use an if-else statement to determine if the string is a palindrome.

word=input("Provide the string")
word=word.lower()
x=len(word)
if word==word[::-1]:
    print("its palendrome")
else:
    print("Its not a palindrome")
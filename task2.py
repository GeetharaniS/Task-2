# Write a python program to calculate the total number of vowels and count of each individual vowels and count of each individual vowel A,E,I,O,U in the string "Guvi Geeks Network Private Limited" ?
#Answers:
def count_vowels(s):
    vowels = "AEIOUaeiou"
    total_vowels = 0

    for char in s:
        if char in vowels:
            total_vowels += 1

    print(f"Total vowels: {total_vowels}")

string = "Guvi Geeks Network Private Limited"
count_vowels(string)

#Create a Pyramid of Numbers from 1 to 20 using For loop?
#Answer:
print(end=" ")
for i in range(1, 21):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#Write a program that takes a string and returns a new string with all the vowels removed.
#Answers:
print(end="\n")
def remove_vowels(s):
    vowels = "AEIOUaeiou"
    answer = ''.join(char for char in s if char not in vowels)
    return answer

a=(input("Enter The String:"))
output = remove_vowels(a)
print(output)

#Write a  program that takes a string and returns the number of unique characters in it.
#Answers:
print(end="\n")
def count_unique_characters(s):
    unique_chars = set(s)
    return len(unique_chars)

a=(input("Enter The String:"))
unique_count = count_unique_characters(a)
print(f"Number of unique characters: {unique_count}")

#Write a program that takes a string and returns True if it is a palindrome, False otherwise.
#Answers:
print(end="\n")
def palindrome(s):
    return s == s[::-1]

a=(input("Enter The Palindrome:"))
print(palindrome(a))

#Write a program that takes two strings and returns the longest common substring between them.
#Answers:
print(end="\n")
def longest_common_substring(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    
    max_length = 0
    end_position = 0
   
    for i in range(len_s1):
        for j in range(len_s2):
            length = 0
            
            while (i + length < len_s1 and j + length < len_s2) and (s1[i + length] == s2[j + length]):
                length += 1
            
            if length > max_length:
                max_length = length
                end_position = i
    
    longest_common_substr = s1[end_position:end_position + max_length]
    
    return longest_common_substr

a=input("Enter ths string1:")
b=input("Enter the string2:")
c=longest_common_substring(a,b)
print(f"Longest common substring: {c}")



#Write a program that takes a string and returns the most frequent character in it.
#Answers:
print(end="\n")
def most_frequent_character(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return max(char_count, key=char_count.get)

a=input("Enter ths string:")
b=most_frequent_character(a)
print(f"Most frequent character: {b}")


#Write a program that takes  True if it is an anagram of another string, False otherwise.
#Answers:
print(end="\n")
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
a=input("Enter ths string1:")
b=input("Enter the string2:")
c=is_anagram(a,b)
print(f"Checking anagram is  {c}")

#Write a program that takes a string and returns the number of words in it.
#Answers:
print(end="\n")
def no_words(s):
    words = s.split()
    return len(words)

a=input("Enter ths string:")
b=no_words(a)
print(f"Number of words: {b}")

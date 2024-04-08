#1. Python program to count the number of vowels
def count_vowels(string):
    vowels='aeiouAEIOU'
    vowels_count={'a':0,'e':0,'i':0,'o':0,'u':0}
    total_vowels=0
    for char in string:
        if char in vowels:
            total_vowels=+1
            char_lower=char.lower()
            vowels_count[char_lower]+=1
    return total_vowels,vowels_count
input_string="Guvi Geeks Network Private Limited"
total,counts=count_vowels(input_string)
print("Total number of vowels=",total)
print("Each vowel count=")
for vowel,count in counts.items():
    print(vowel,":",count)       
            
#2. Pyramid of numbers
height = 20
for i in range (1,height+1):
    print(*range(1,i+1))
    
#3. Takes a string and returns it without vowels
    
def remove_vowels(input_string):
    vowels = 'aeiouAEIOU'
    answer = ''
    for char in input_string:
        if char not in vowels:
            answer +=char
    return answer
input_string = input("Write here:")
no_vowels = remove_vowels(input_string)
print("String without any vowels:", no_vowels)

#4. Takes a string and returns the number of unique characters in it
def unique_characters_present(input_string):
    unique_characters = set(input_string)
    return len(unique_characters)
input_string = input("Write a string:")
unique_characters = unique_characters_present(input_string)
print("Unique character count is",unique_characters)

#5. Takes a string and return true if it is a palindrome, false if not
def palindrome(input_string):
    return input_string == input_string[::-1]
input_string = input("Write a string:")
print (palindrome(input_string))

#6. Takes 2 strings and returns the longest common sub string
def long_common_substring(str1,str2):
    a=len(str1)
    b=len(str2)
    c=[[0]*(b+1) for _ in range(a+1)] 
    length=0
    index=0
    for x in range(1,a+1):
        for y in range(1,b+1):
            if str1[x-1] == str2[y-1]:
                c[x][y] = c[x-1][y-1]+1
                if c[x][y] > max_length:
                    max_length = c[x][y]
                    end_index = x
                else:
                    c[x][y]=0
    longest_substring=str1[end_index-max_length:end_index]
    return longest_substring
    
str1=input("Write the longest string 1") 
str2=input("Write the longest string 2")
final_output=longest_common_substring(str1,str2)
print("The longest common substring is:",final_output)

#7. Takes a string and returns most frequent character
def freq_character(input_string):
    return max(set(input_string),key=input_string.count)
input_string=input("Write a string")
freq_character=freq_character(input_string)
print("The most frequent character is:",freq_character)    

#8. Takes a string and returns true if it is an anagram else false
def anagram(str1,str2):
    str1=str1.lower()
    str2=str2.lower()
    return sorted(str1) == sorted(str2)
str1=input("Enter the first string")
str2=input("Enter the second string")
print("Answer",anagram(str1,str2))

#9. Takes a string and returns the number of words in it
def num_words(input_string):
    words = input_string.split()
    return len(words)
input_string=input("Write the string")
count_words=num_words(input_string)
print("The total number of words in the string is:",count_words)

#END OF SESSION 5 TASK
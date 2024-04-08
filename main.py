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
            


height = 20
for i in range (1,height+1):
    print(*range(1,i+1))
    
    
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


def unique_characters_present(input_string):
    unique_characters = set(input_string)
    return unique_characters
input_string = input("Write a string:")
unique_characters = unique_characters_present(input_string)
print("Unique characters are",unique_characters)

def palindrome(input_string):
    return input_string == input_string[::-1]
input_string = input("Write a string:")
print (palindrome(input_string))
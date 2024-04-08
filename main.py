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
            

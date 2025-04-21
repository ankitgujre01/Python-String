string = input("Enter a string: ")

vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
vowel_count = 0
consonant_count = 0
for char in string:
    if char in vowels:
        vowel_count += 1
    # elif char in consonants:
    #     consonant_count += 1
    else:
        consonant_count += 1
# print(f"Number of vowels: {vowel_count}")
# print(f"Number of consonants: {consonant_count}")
print("Number of Vowels: ", vowel_count)
print("Number of Consonants: ", consonant_count)
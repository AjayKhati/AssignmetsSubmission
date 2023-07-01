#Write a Python function that takes in a string and returns the string with all the vowels removed.

def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in input_string if char not in vowels)

input_str = input("Enter a string: ")
result = remove_vowels(input_str)
print("String with vowels removed:", result)


#OUTPUT

Enter a string: ajay singh
String with vowels removed: jy sngh
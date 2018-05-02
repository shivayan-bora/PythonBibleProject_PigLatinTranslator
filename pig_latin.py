# Get sentence from user
original = input("Please enter sentence to convert to Pig Latin: ").strip().lower()

# Split sentence into individual words
words = original.split()

# Loop through the words and convert to pig latin
new_words = []

# Rules: 1. If it starts with a vowel, just add "yay" 
#        2. Otherwise, move the first consonant cluster to end and add "ay"
for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos += 1
            else:
                # Similar to Java break
                break
        
        consonant = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + consonant + "ay"
        new_words.append(new_word)

# Stick words back together
# The join() method concatenates each of the strings present in the 
# iterable data structure using a separator which is provided in the beginning
# e.g. in the below example, all the strings in the new_words list will be 
# concatenated with a space as a separator
final_string = " ".join(new_words)

# Output the final string
print(final_string)
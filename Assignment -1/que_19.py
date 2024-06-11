import string
# Input string
str = input("enter the string")

# Remove punctuation from the string
no_punct = "".join(char for char in str if char not in string.punctuation)

# Print the string without punctuation
print(no_punct)
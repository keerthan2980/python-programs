def count_words(sentence):
    words=sentence.strip().split()
    return len(words)
print(count_words("welcome to my world"))

text = "###Hello###"
print(text.strip("#"))  
# Output: 'Hello'

text1=" Apple  "
print(text1)#it will print the spaces also
text2="  Apple2  "
print(text2.strip())


# strip() - Removes leading and trailing spaces.
# split() - Splits the sentence into words using whitespace as a delimiter.
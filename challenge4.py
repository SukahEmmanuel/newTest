#Create a function unique_words that takes a string of text as input. The function should convert the
#  string to a set of words, ignoring case and punctuation. It should then return the number of 
# unique words in the text. For example, the sentence "The quick brown fox jumps over the lazy dog." 
# has 8 unique words.
import string
def unique_words(text):
    
    # implement a translation map for translate()
    translator = str.maketrans('', '', string.punctuation) 
    #apply mpa to remove punctuation, convert to lowercase, split into words
    cleaned_text = text.translate(translator).lower()
    words = cleaned_text.split()
    unique = set(words)
    return len(unique)

userInput = input("Enter a string of text: ")
print(f"The number of unique words in the text is: {unique_words(userInput)}")
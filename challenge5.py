#Write a function word_frequency that takes a string of text. The function should return a dictionary 
# where the keys are the unique words in the text and the values are the number of times each word 
# appears. The word matching should be case-insensitive.

import string
def word_frequency(text):
    myDictionary = {}
    translator = str.maketrans('','',string.punctuation)
    cleaned_text = text.translate(translator).lower()
    words = cleaned_text.split()
    unique_words = set(words)
    for unique_word in unique_words:
        myDictionary[unique_word] = words.count(unique_word)
    return myDictionary

    
message = input("Enter some text: ")
print(f"Here are the unique words: {word_frequency(message)}")

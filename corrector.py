import nltk
from nltk.corpus import words
from nltk.metrics.distance import edit_distance

nltk.download("words")

# List of words in the NLTK words corpus
dictionary = words.words()

def correct_word(input_word):
    closest_word = min(dictionary, key=lambda word: edit_distance(input_word, word))
    return closest_word

# Test the spell-checking AI
input_word = "orang"
corrected_word = correct_word(input_word)

print(f"Input word: {input_word}")
print(f"Corrected word: {corrected_word}")

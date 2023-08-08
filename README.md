# AI_auto_correct

Task 2 : Auto Corrector tool

In this code, we use the Natural Language Toolkit (NLTK) library to check if a given word exists in WordNet, a lexical database for English.
If the word is not found, we generate a list of suggestions from WordNet and calculate the edit distance (number of single-character edits required
to transform one word into another) between the misspelled word and each suggestion. 
Finally, we return the suggestion with the lowest edit distance as the corrected word.

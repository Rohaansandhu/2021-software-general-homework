# Set the variable in_list to whatever value you want. Let's use 
# [ 5, 2, 3, 1, 4, 6, 8, 7 ] as an example.

# Use for loops, while loops, and whatever else we've learned to 
# set the variable x to the length of in_list - but you may NOT use len! 
# Try to mimic the behavior of len.

def lstlength():
    in_list = [5, 2, 3, 1, 4, 6, 8, 7]
    x = 0
    for i in in_list:
        x += 1
    print(x)

lstlength()
################################################
# Create a program to accept words from a user, and add them to a dictionary. 
# At the end, use print(mydict) to print out the user's work to them

def translate():
    print("Dictionary Translator!")
    mydict = {}
    word_prompt = True
    add_items = True
    #mainloop for prompting words and translations
    while True:
        if word_prompt:
            #inputs
            word = input("Enter a word: ")
            translation = input("Enter the word's translation: ")
            #checks if words or translations are already in dictionary
            for key, value in mydict.items():
                if key == word:
                    print("This word is already in use")
                    add_items = False
                    word_prompt = False
                    continue
                elif value == translation:
                    print("This translation is already in use")
                    add_items = False
                    word_prompt = False
                    continue
            #makes sure word has no spaces
            spaces = len(word.split())
            if spaces > 1:
                print("Do not use spaces in the key")
                add_items = False        
        #asks if more words and translations want to be added
        more_words = input("Would you like to add another word? (y/n): ")
        if add_items:
            mydict[word] = translation
        if more_words == "y":
            word_prompt = True
            add_items = True
            continue
        elif more_words == "n":
            break
        else:
            word_prompt = False
            continue
    #translates sentence
    newdict = {}
    sentence = input("Enter a sentence: ")
    sentencesplit = sentence.split()
    pos = -1
    for i in sentencesplit:
        pos += 1
        for key, value in mydict.items():
            if i == key:
                tword = value
                realpos = pos
                newdict[realpos] = tword
            else:
                continue
    for key, value in newdict.items():
        sentencesplit.pop(key)
        sentencesplit.insert(key, value)
    translation = " "
    print("Your translation: " + translation.join(sentencesplit))
    
translate()






################################################
# Extend your dictionary program from assignment #2 to have some added capabilities:

# Make sure the user cannot enter more than one translation for the same word, 
# in either direction. For example, if ‘dog’: ‘Hund’ is already an entry in the 
# dictionary, then adding a new translation for ‘dog’ OR another word that translates 
# to ‘Hund’ should fail.

# Make sure the user cannot input a key that contains a space, but a value that 
# contains a space is acceptable. So adding ‘the dog’ : ‘Hund’ should fail, but 
# ‘dog’ : ‘der Hund’ is fine.



################################################
# Instead of printing out the dictionary when the program is done, ask the user 
# for a sentence and “translate” it, word-by-word, as output. 

# If a word has no translation, use the word unchanged.

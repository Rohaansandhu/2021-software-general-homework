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
# iaushduifhuasd
################################################
# Create a program to accept words from a user, and add them to a dictionary. 
# At the end, use print(mydict) to print out the user's work to them

def translate():
    print("Dictionary Translator!")
    mydict = {}
    w = True
    z = 0
    d = True
    l = True
    while w:
        if d == True:
            a = input("Enter a word: ")
            b = input("Enter the word's translation: ")
            for key, value in mydict.items():
                if key == a:
                    print("This key is already in use")
                    l = False
                    d = False
                    continue
                elif value == b:
                    print("This value is already in use")
                    l = False
                    d = False
                    continue
            x = a.split()
            x = len(x)
            if x > 1:
                print("Do not use spaces in the key")
                l = False        
        c = input("Would you like to add another word? (y/n): ")
        if l:
            mydict[a] = b
        if c == "y":
            d = True
            l = True
            continue
        elif c == "n":
            w = False
        else:
            d = False
            continue
    place = {}
    z = input("Enter a sentence: ")
    r = z.split()
    pos = -1
    for i in r:
        pos += 1
        for key, value in mydict.items():
            if i == key:
                tword = value
                realpos = pos
                place[realpos] = tword
            else:
                continue
    if realpos == -1:
        print(z)
        quit()
    for key, value in place.items():
        r.pop(key)
        r.insert(key, value)
    translation = " "
    print("Your translation: " + translation.join(r))

    
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

def advanced_slice():
    # Advanced Slicing:
    # Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
    # a. Extract the letters 'hij'.
    # b. Extract every second letter starting from 'a' to 'm'.
    # c. Reverse the entire string using slicing.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    print (alphabet[7:10])

    print (alphabet[0:13:2])

    print (alphabet[::-1])
    print (alphabet[83:])
    # Problem Set 2: Extracting Information
    # From Descriptions:
    # Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"

    person = 'Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy'

    # Manipulating Words:
    # Given the string info = "Python is fun. Fun is good. Good is subjective.",
    # a. Extract the word 'subjective' without knowing its exact position.
    # b. Extract every third word.
    # c. Reverse the positions of the words, but keep the characters in each word in the same order.

    bad= 'Python is fun. Fun is good. Good is subjective.'

    print (bad[36:])

    every_third_word = bad.split()[::3]
    print(every_third_word)

    every_third_words = bad.split()[::-1]
    print(every_third_words)
def problem4():
     # Problem Set 4: String Properties and Advanced Operations
    # Repetition:
    # Concatenate the word "Iteration" 7 times.
    result = "Iteration" * 7
    print(result)


    # Word Search:
    # Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
    quote = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

    print("moonlight" in quote)  

    # Length and Count:
    # a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
    # b. Count the number of times the letter 'i' appears in the same word/phrase.

    phrase= "Supercalifragilisticexpialidocious"
    lenght_of_phrase = len(phrase)
    count_of_i=phrase.count('i')
    print(count_of_i)
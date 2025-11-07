def problem3():
        # Problem Set 3: String Methods
    # Upper & Lower:
    # Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
    good = 'MAY THE FORCE BE WITH YOU'
    print (good.lower())

    # String Joining and Splitting:
    # Given the list motto = ["Make", "haste", "slowly."],
    # a. Convert the list into a single string.
    # b. Now, split the string at every occurrence of the letter 'a'.
    motto = 'Make haste slowly'

    motto_string= ''.join(motto)
    print (motto)
    # Replacing Words:
    # Modify the sentence: "Life is what happens when you are busy making other plans."
    # a. Replace "busy" with "distracted".
    # b. Replace "plans" with "mistakes".
    word="Life is what happens when you are busy making other plans."
    modified_sentence=word.replace("busy","distracted").replace("plans","mistakes")
    print (modified_sentence)
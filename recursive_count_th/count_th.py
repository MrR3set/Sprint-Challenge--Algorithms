'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    if len(word) == 0:
        return 0

    # If the word starts with T check what the second letter is
    if word[0] == "t":
        if len(word) == 1:
            return 0  # If the word has len 1 return 0

        if word[1]=="h":
            return 1+count_th(word[2:]) # If the second letter is h then add 1 to the count and call count_th with the rest of the stuff
        else:
            return 0+count_th(word[1:])

    return count_th(word[1:])


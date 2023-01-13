#Reverses a sentence and ignore excess white space
def rev(words):
    i = 0
    length = len(words) -1
    revs_word = ''
    while length >= i:
        revs_word += words[length] + ' '

        length -= 1

    return revs_word
        
def rev_word(s):
    words = []
    spaces = [' ']
    length = len(s)
    
    i = 0

    while i < length:

        if s[i] not in spaces:
            word_start = i

            while i < length and s[i] not in spaces:

                i += 1

            words.append(s[word_start:i])

        i += 1

    return rev(words)
        

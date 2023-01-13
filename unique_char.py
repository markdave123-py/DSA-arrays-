def uni_chars(s):
    check = {}
    count = 0
    key_check = 0

    for char in s:
        if char in check:
            check[char] += 1

        else:
            check[char] = 1

    for key in check:
        count += check[key]
        key_check += 1
    return count == key_check

#Alternatively
def uni_char2(s):
    return len(set(s)) == len(s)
#Alternatively
def uni_char3(s):

    chars = set()
    for letter in s:
        if letter in chars:
            return False
        chars.add(letter)
    return True
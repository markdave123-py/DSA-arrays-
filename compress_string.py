def dict_to_str(freq):
    string = ''
    for key in freq:
        string = string + str(key) + str(freq[key])
    return string
    
def compress(s):
    i = 0
    freq = {}
    high = len(s)

    if high == 0:
        return ''

    if high == 1:
        return s+'1'

    while i < high:
        new_start = s[0]
        if new_start == s[i]:
            if new_start in freq:
                freq[new_start] += 1

            else:
                freq[new_start] = 1
        else:
            new_start = s[i]
            
            if new_start in freq:
                freq[new_start] += 1

            else:
                freq[new_start] = 1           
        i += 1

    return dict_to_str(freq)
print(compress('AAaBBBBCCcccDDBBb'))
#Alternatively 

def compress2(s):

    r = ''
    l = len(s)
    
    if l == 0:
        return ''
    if l == 1:
        return s+'1'
    count = 1
    i = 1

    while i < l:
        if s[i] == s[i-1]:
            count += 1

        else:
            r = r + s[i-1] + str(count)

            count = 1

        i += 1
    r = r + s[i-1] + str(count)

    return r
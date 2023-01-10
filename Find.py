#Finding the missing number between two arrays a1 and a2
#where a2 is a shuffled version  and a random number  removed from a1

def finder1(a1,a2):
    a1.sort()
    a2.sort()

    for num1, num2 in zip(a1,a2):
        if num1 != num2:
            return num1

    return a1[-1]


def finder(a1,a2):
    seen = {}
    for num in a1:
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1

    for num1 in a2:
        seen[num1] -= 1

    for key in seen:
        if seen[key] == 1:
            return key
            

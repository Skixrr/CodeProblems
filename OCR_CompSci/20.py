word = input('Enter word here: ')
word = word.upper()
def TwoPointer(wrd):
    i = 0
    j = len(wrd) - 1
    palindrome = True
    while i != j:
        if wrd[i] == wrd[j]:
            i += 1
            j -= 1
        else:
            palindrome = False
            break
        return palindrome

def RevStr(wrd):
    temp = wrd[::-1]
    if temp == wrd:
        return True
    else:
        return False
    
print(TwoPointer(word))
print(RevStr(word))

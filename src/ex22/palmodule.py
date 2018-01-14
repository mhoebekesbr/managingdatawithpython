def buildPalindrome(letters=''):
    revletters = ''.join(reversed(list(letters)))
    return letters +' '+ revletters

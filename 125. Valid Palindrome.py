def isvalidpalindrome(s):
    intake = s.strip()
    intake = intake.lower()
    intake = ''.join(char for char in intake if char.isalnum())
    if intake[0::] == intake[::-1]:
        return True
    else:
        return False

sen = "0p"

print(isvalidpalindrome(sen))



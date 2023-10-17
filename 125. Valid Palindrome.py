def isvalidpalindrome(s):
    intake = s.strip()
    intake = intake.lower()
    intake = ''.join(char for char in intake if char.isalnum())
    if intake[0::] == intake[::-1]:
        return True
    else:
        return False

###################################################################################
#                        Leet Code Difficulty Level = Easy                        #  
#                        Runtime = 28 ms    [ > 69.93%]                           #
#                        Memory = 15.08 MB   [ > 39.70%]                          #
###################################################################################   


# This program is to prove if the letters given is a palindrome or not
def is_palindrome(letters):
    precondition(type(letters)==type("string"))
    
    if len(letters)== 0 or len(letters)== 1:
        return True
    elif letters[0]==letters[-1]:
        return is_palindrome(letters [1:-1])
    else:
        return False
    
    postcondition(result == (letters==letters[::-1]))
   

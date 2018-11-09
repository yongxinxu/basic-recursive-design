"""
##############################################################################
#
>>> is_palindrome("sees")
True

>>> is_palindrome("livedondecaffacednodevil")
True

>>> is_palindrome("amanaplanacanalpanama")
True

>>> is_palindrome("aaa")
True

>>> is_palindrome("love")
False

>>> is_palindrome("a")
True

>>> is_palindrome("")
True


#
##############################################################################


##############################################################################
#
# Design notes: 
# 1. Identify a smaller instance of problem: letter [1, -1]
# 2. Express solution to general problem in terms of solution to smaller instance: letter[1] == letter[-1]
# 3. base cases, smallest cases, no recursion: len(letter)==1 or len(letter)== 0
# 4. answer to base case: True
# 5. show that program eventually reaches base case: subtracting the front letter and the last letter of the string, will eventually reach empty or one character string.
#
##############################################################################

"""

# make Python look in the right place for logic.py, or complain if it doesn't
try:
    import sys
    sys.path.append('/home/courses/python')
    from logic import *
except:
    print "Can't find logic.py; if this happens in the CS teaching lab, tell your instructor"
    print "   If you are using a different computer, add logic.py to your project"
    print "   (You can download logic.py from http://www.cs.haverford.edu/resources/software/logic.py)"
    sys.exit(1)
    
# This program is to prove if the letters given is a palindrome or not
def is_palindrome(letters):
    precondition(type(letters)==type("string"))
    
    
    if len(letters)== 0 or len(letters)== 1:
        return True
    elif letters[0]==letters[-1]:
        return is_palindrome(letters [1:-1])
    else:
        return False
    

    

#  Lab 3, Question 1b --- REPLACE THE REST OF THIS FUNCTION WITH YOUR ANSWER


    postcondition(result == (letters==letters[::-1]))
    



# User interface for the palindrome function
def palindrome_ui():
    if __name__ == "__main__":
        print "Type 1 to run your test-suite, press 2 to type in your own tests:"
        answer = raw_input()
        if answer in ['1']:  
            _test()
        else:
            print "Please input a possible palindrome: "
            trial_text = raw_input()
            letters_only = lower_case_letters(trial_text)
            if is_palindrome(letters_only):
                print "The text '"+letters_only+"' is a palindrome"
            else:
                print "The text '"+letters_only+"' is not a palindrome."

"""
    make something all lower case letters, e.g.

>>> lower_case_letters('kayak')
'kayak'
>>> lower_case_letters('A man, a plan, a canal: Panama!')
'amanaplanacanalpanama'
"""

def lower_case_letters(text):
    if text == '':
        return ''
    else:
        first = text[0]
        rest  = text[1:len(text)]
        if first in 'abcdefghijklmnopqrstuvwxyz':  # already lower case
            return first + lower_case_letters(rest)
        elif first in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': # upper-case
            # lower(first) turns, for example, "D" into "d"
            from string import lower
            return lower(first) + lower_case_letters(rest)
        else:   # otherwise skip first element, as it's not a letter
            return lower_case_letters(rest)

# mostly copied from  http://docs.python.org/lib/module-doctest.html

def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!"
    else:
        print "Rats!"

# tests may or may not be chosen by the user interface...
if __name__ == "__main__": palindrome_ui()


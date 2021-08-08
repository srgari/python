#%%
import re
#%% Basics: telefone matcher

text = [
    '(11) 9 7326-1414',
    '11973937860'
    ]
pattern = r'^\D?\d{2}\D{0,2}\d\D?\d{4}\D?\d{4}'


def basics(text, pattern):
    r"""
    Let's break this hyeroglyphs down! Fuckers!
    Bear in mind: these symbols can mean sth else    
    depending on the context!
    
    Symbol(s) : metacharacter(s)                - what it does
    _________________________________________________________________________________
    |^|       : ?                               - Strings must start with the next element
    |\D|      : shorthand                       - whatever is NOT a number
    |?|       : quantifier                      - occuring 0 or 1 times  
    |\d|      : shorthand                       - whatever IS a number
    |{2}|     : quantifier                      - occuring 2 times
    |\D{0,2}| : shorthand + quantifier          - NOT a number occuring between 0 and 2 times
    |\d\D?|   : two shorthand and one quantifer - a number, followed or not by whaterver is NOT a number 
    
    """
    comp = re.compile(pattern)
    findall = comp.findall(text)
    lala = comp.search(text)
    
    return findall, lala 

if __name__ == "__main__":
    for x in text:
        basics(x, pattern)



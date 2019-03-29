def abbreviation(a, b):
    o = a
    f  = False
    if b in a.upper():
        f = True
    else:
        return "NO"
    if f:
        for e in o:
            print(e)
            if e.isupper():
                return "NO"
    return "YES"

    

print(abbreviation("BEFGH","EFG"))
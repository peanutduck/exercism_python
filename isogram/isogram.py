def is_isogram(string):
    string = [c.lower() for c in string if c.isalpha()]
    return len(string) == len(set(string))

    

    

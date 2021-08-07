def is_isogram(string):
    # make string lower and remove special characters
    #string = string.lower().replace(' ', '').replace('-', '')
    string = [c.lower() for c in string if c.isalpha()]

    #if len(string) == len(set(string)):
    #    return True
    #return False

    return len(string) == len(set(string))

    

    

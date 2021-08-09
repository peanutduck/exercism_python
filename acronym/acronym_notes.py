import re

def abbreviate(words):
    return ''.join([x[0] for x in re.findall("[A-Z]+[a-z\']*|[a-z]+", words)]).upper()
#    return "".join([w.upper()[0] for w in re.sub("[-_]", " ", words).split()])



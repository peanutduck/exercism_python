tmp = [("AEIOULNRST", 1), ("DG", 2), ("BCMP", 3), ("FHVXYW", 4), ("K", 5), ("JX", 8), ("QZ", 10)]

# create letter with dictionary
# {'A': 1, 'C': 3, 'B': 3, 'E': 1, ... }
points = {alphabet:score for alphabets, score in tmp for alphabet in alphabets}

def score(word):
    return sum(points[alphabet] for alphabet in word.upper())

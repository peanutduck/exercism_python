drops = ((3, 'Pling'), (5, 'Plang'), (7, 'Plong'))
#drops = {3: 'Pling', 5: 'Plang', 7: 'Plong'}

def convert(number):
    # tuple
    #speak = [s for f, s in drops if number % f == 0]

    # dict
    #speak = [s for f, s in drops.items() if number % f == 0]

    #return "".join(speak) or str(number)
    #return "".join(speak) if speak else str(number)

    # gen expression
    return "".join(s for f, s in drops if number % f == 0) or str(number)

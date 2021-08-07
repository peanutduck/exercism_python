def distance(strand_a, strand_b):

    if len(strand_a) != len(strand_b):
        raise ValueError('not same length')
    
    # sum([True, True]) ----> 2
    return sum(i != j for i, j in zip(strand_a, strand_b))

    #return sum(1 for i, j in zip(strand_a, strand_b) if i != j)

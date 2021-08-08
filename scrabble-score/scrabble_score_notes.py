from enum import IntEnum

class Scrabble(IntEnum):
    """
        >>> x = [Scrabble['A'], Scrabble['A']]
        >>> x
        [<Scrabble.A: 1>, <Scrabble.A: 1>]
        >>> sum(x)
        2
    """
    A = E = I = O = U = L = N = R = S = T = 1
    D = G = 2
    B = C = M = P = 3
    F = H = V = W = Y = 4
    K = 5
    J = X = 8
    Q = Z = 10

def score(word): 
    return sum(Scrabble[char.upper()] for char in word)


from operator import add, mul, truediv

def divide_all(n, ds):
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')

def reduce(f, s, initial):
    """Combine elements of s pairwise using f, starting with initial.
    
    E.g., reduce(mul, [2, 4, 8], 1) is equivialent to mul(mul(mul(1, 2), 4), 8).
    
    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(add, [1, 2, 3, 4], 0)
    10
    """
    for x in s:
        initial = f(initial, x)
    return initial

def reduce_1(f, s, initial):
    """Combine elements of s pairwise using f, starting with initial.
    
    E.g., reduce(mul, [2, 4, 8], 1) is equivialent to mul(mul(mul(1, 2), 4), 8).
    
    >>> reduce_1(mul, [2, 4, 8], 1)
    64
    >>> reduce_1(add, [1, 2, 3, 4], 0)
    10
    """
    if not s:
        return initial
    else:
        return reduce_1(f, s[1:], f(initial, s[0]))
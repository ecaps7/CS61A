def count_partitions(n, m):
    """Count partitions.
    
    >>> count_partitions(6, 4)
    9"""
    if n < 0 or m == 0:
        return 0
    else:
        exact_match = 0
        if n == m:
            exact_match = 1
        with_m = count_partitions(n - m, m)
        without_m = count_partitions(n, m - 1)
        return exact_match + with_m + without_m

def list_partions(n, m):
    """List partions.
    >>> for p in list_partions(6, 4): print(p)
    [2, 4]
    [1, 1, 4]
    [3, 3]
    [1, 2, 3]
    [1, 1, 1, 3]
    [2, 2, 2]
    [1, 1, 2, 2]
    [1, 1, 1, 1, 2]
    [1, 1, 1, 1, 1, 1]
    """
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [[m]]
        with_m = [p + [m] for p in list_partions(n - m, m)]
        without_m = list_partions(n, m - 1)
        return exact_match + with_m + without_m
    
def partions(n, m):
    """List partions.

    >>> for p in partions(6, 4):
    ...     print(p)
    ...
    2 + 4
    1 + 1 + 4
    3 + 3
    1 + 2 + 3
    1 + 1 + 1 + 3
    2 + 2 + 2
    1 + 1 + 2 + 2
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 1 + 1 + 1
    """
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [str(m)]
        with_m = [p + ' + ' + str(m) for p in partions(n - m, m)]
        without_m = partions(n, m - 1)
        return exact_match + with_m + without_m
    
def yield_partitions(n, m):
    """Yield partions.
    
    >>> for p in partions(6, 4):
    ...     print(p)
    ...
    2 + 4
    1 + 1 + 4
    3 + 3
    1 + 2 + 3
    1 + 1 + 1 + 3
    2 + 2 + 2
    1 + 1 + 2 + 2
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 1 + 1 + 1
    """
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in yield_partitions(n - m, m):
            yield p + ' + ' + str(m)
        yield from yield_partitions(n, m - 1)
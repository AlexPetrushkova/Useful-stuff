def triplets():
    """
    Finds the first six Pythagorean triplets where a < b < c <= 20
    """
    lst = list()
    for a in range (1, 21):
        for b in range (a, 21):
            for c in range(b, 21):
                if a*a + b*b == c*c and a < b:
                    lst.append((a, b, c))
    return lst


print(triplets())
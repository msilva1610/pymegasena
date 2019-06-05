import itertools

stuff = [1, 2, 3, 4, 5, 6]
for L in range(0, len(stuff)+1):
    for subset in itertools.combinations(stuff, L):
        print(subset)
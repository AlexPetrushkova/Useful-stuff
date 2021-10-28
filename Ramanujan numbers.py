cache = { }
twice = { }

a = 0
while len(twice) < 5:
    a += 1
    b = 0
    while b < a:
        b += 1
        n = a ** 3 + b ** 3

        if n in cache:
            twice[n] = [cache[n], [a, b]]
        else:
            cache[n] = [a, b]

for n in twice: 
    print(n, twice[n])


def f(s, c, a):
    if s >= 129: return c % 2 == a % 2
    if c == a: return 0
    h = [f(s +1, c + 1, a), f(s + 2, c + 1, a)]
    return any(h) if (c + 1) % 2 == a % 2 else all(h) #ALL - удачник, ANY - неудачник


for s in range(1, 129):
    for a in range(1, 5):
        if f(s, 0, a) == 1:
            print(s, a)




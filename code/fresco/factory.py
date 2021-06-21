def factory(n = 0):

    def current():
        print(f"current n : {n}")
        print(f"type(n) : {type(n)}")
        return n

    def counter():
        nonlocal n
        print(f"counter n : {n}")
        n = n + 1
        return n

    return current, counter

f_current, f_counter = factory(int(input()))


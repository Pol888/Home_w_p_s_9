a = 70

def f():
    a = 10
    def ind():
        nonlocal a
        a = 8
        a += 1
        print(a)

    ind()
    print(a)
    return


f()
print(a)
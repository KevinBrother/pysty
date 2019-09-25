def foo():
    a, b = 0, 1
    while True:
        a,b = b, a + b
        yield a

def main():
    g = foo()
    for _ in range(10):
        print(g)
        print(foo)
        # print(next(g))

if __name__ == "__main__":
    main()

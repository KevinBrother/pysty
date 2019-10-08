def foo():
    while True:
        x = yield
        print("value:",x)

g = foo()

next(g)
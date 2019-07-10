# utf-8

def foo():
    b = 'hello'

    def bar():  # Python中可以在函数内部再定义函数
        c = True
        print(a)
        print(b)
        print(c)

    bar()

if __name__ == '__main__':
    a = 100
    # print(b)  # NameError: name 'b' is not defined
    foo()
""" 
def main():
    # Todo: Add your code here
    pass


if __name__ == '__main__':
    main() 
"""
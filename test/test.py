def abc():
    a = 1
    b = 2
    return a, isTrue()

def isTrue():
    return 1==1


def test_else_finally3():
    try:
        print(1)
        #return 1
    except:
        print(2)
        #return 2
    else:
        print(3)
        #return 3
    finally:
        print(0)
        return 0



def main():
    # print(abc())
    print(test_else_finally3())

if __name__ == "__main__":
    main()
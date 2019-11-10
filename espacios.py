def foo():
    # global a
    # a = 5

    def bar():
        a = 7

        def baz():
            nonlocal a
            a = 9
            print("en baz", a)

        baz()
        print("en bar", a)

    bar()
    print("en foo", a)


a = 3
foo()
print("afuera", a)

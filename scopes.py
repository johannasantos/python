

def func():
    x = 2
    print(x, j)

j = 3
func()


class F:
    x = 4

    def foo(self):
        print(self.x, j)


f = F()
f.foo()


def foo():
    x = 5

    def bar():
        print(x, j)

    bar()


foo()

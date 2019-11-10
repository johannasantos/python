

# def foo():
#     x = 3
#
#     def bar():
#         print(x)
#
#     return bar
#
# f = foo()
# f()


def gen_potenciaciones(exp):

    def bar(n):
        return n ** exp

    return bar

cuad = gen_potenciaciones(2)
print(cuad(5))
cubo = gen_potenciaciones(3)
print(cubo(5))

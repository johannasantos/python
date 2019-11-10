# def foo(a, b):
#     print(a, b)
#
#
# x = foo(3, 4)
# print(x)


# def foo(a, b=5, c=9):
#     print(a, b, c)
#
#
# foo(1, 2, 3)
# foo(1, 2)
# foo(1)
# foo(1, c=3)
# foo(c=3, a=3)


# def foo(a, b, *x, **y):
#     print(a, b, x, y)
#
#
# foo(1, 2)
# foo(1, 2, 3, 4, 5, 6)
# foo(1, 2, c=3)
# foo(1, b=1, c=3)


# def foo(a, b):
#     print(a, b)
#
# t = (1, 2)
# foo(*t)
# # t = (1, 2, 3)
# # foo(*t)
# d = {'a': 1, 'b': 2}
# foo(**d)
# # d = {'a': 1, 'b': 2, 'c': 4}
# # foo(**d)
# foo(1, 2, a=3)

# def foo(a, b, *, c):
#     print(a, b, c)
#
#
# foo(1, 2, c=3)


# def foo(a):
#     a -= 1
#     print(a)
#     # if a > 0:
#     #     foo(a)
#     foo(a)
#
#
# foo(4)


# lambda <params>: <resultado>


# def foo(a, b=[]):
#     if a > 0:
#         b.append(a ** 2)
#     print(b)

def foo(a, b=None):
    if b is None:
        b = []
    if a > 0:
        b.append(a ** 2)
    print(b)


foo(2, [2, 3])
foo(1, [0])
foo(1)
foo(2)
foo(2)
foo(2)

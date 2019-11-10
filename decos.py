# def foo(func_externa):
#
#     def bar(*args, **kwargs):
#         print("==== log, llamada", func_externa, args, kwargs)
#         result = func_externa(*args, **kwargs)
#         print("==== log, result", result)
#         return result
#
#     return bar
#
#
# def cuad(nro):
#     return nro ** 2
#
# def cubo(nro):
#     return nro ** 3
#
# def multiexp(nro, exp):
#     return nro ** exp
#
# cuad = foo(cuad)
# print(cuad(3))
# cubo = foo(cubo)
# print(cubo(4))
# multiexp = foo(multiexp)
# print(multiexp(2, exp=4))



# def foo(func_externa):
#
#     def bar(*args, **kwargs):
#         print("==== log, llamada", func_externa, args, kwargs)
#         result = func_externa(*args, **kwargs)
#         print("==== log, result", result)
#         return result
#
#     return bar
#
#
# @foo
# def cuad(nro):
#     return nro ** 2
#
# @foo
# def cubo(nro):
#     return nro ** 3
#
# @foo
# def multiexp(nro, exp):
#     return nro ** exp
#
# print(cuad(3))
# print(cubo(4))
# print(multiexp(2, exp=4))


# def logueadora(marcador):
#
#     def logueadora_posta(func_externa):
#
#         def bar(*args, **kwargs):
#             print(marcador*10, "log, llamada", func_externa, args, kwargs)
#             result = func_externa(*args, **kwargs)
#             print(marcador*10, "log, result", result)
#             return result
#
#         return bar
#     return logueadora_posta
#
#
# @otracosa
# @logueadora("=")
# def cuad(nro):
#     return nro ** 2
#
# @logueadora("-")
# def cubo(nro):
#     return nro ** 3
#
#
# print(cuad(4))
# print(cubo(4))


# def foo(func_externa):
#
#     def bar(*args, **kwargs):
#         print("==== log, llamada", func_externa, args, kwargs)
#         try:
#             result = func_externa(*args, **kwargs)
#         except Exception as err:
#             print("==== log, pumba", repr(err))
#             raise
#         else:
#             print("==== log, result", result)
#             return result
#
#     return bar
#
#
# @foo
# def calculo(nro):
#     return (20 / nro) ** 2
#
# print(calculo(5))
# print(calculo(0))

def foo(cls):
    attrs = [x for x in dir(cls) if x.isupper()]
    print("==== atrs", attrs)
    for attr in attrs:
        valor_original =  getattr(cls, attr)
        prop = property(lambda self: valor_original)
        setattr(cls, attr, prop)

    return cls


@foo
class C:
    color = "red"
    TIMEOUT = 5

c = C()

print(dir(C))
print(c.color, c.TIMEOUT)
c.color = "blue"
print(c.color, c.TIMEOUT)
c.TIMEOUT = 100
print(c.color, c.TIMEOUT)

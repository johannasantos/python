# def func(n):
#     res = []
#     i = 0
#     while i < n:
#         res.append(i)
#         i += 1
#     return res
#
# print("func", func)
# nros = func(5)
# print("nros", nros)
# print("total", sum(nros))

# def func(n):
#     i = 0
#     while i < n:
#         yield i
#         i += 1
#
# print("func", func)
# nros = func(5)
# print("nros", nros)
# print("total", sum(nros))


# def func(n):
#     i = 0
#     while i < n:
#         if i % 2 == 0:
#             yield i
#
#         yield i
#         i += 1
#
# print("con dobles pares", list(func(10)))


# def func(n):
#     i = 0
#     while i < n:
#         deafuera = yield i
#         if deafuera is not None:
#             i = deafuera
#         i += 1
#
# gen = func(3)
# next(gen)
# gen.throw(ValueError("fruta"))



# class MiGen:
#
#     def __init__(self, n):
#         self.limit = n
#         self.idx = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         idx = self.idx
#         self.idx += 1
#         if self.idx > self.limit:
#             raise StopIteration
#         return idx


# gen = MiGen(4)
# print(next(gen))
# print(next(gen))
# print(list(gen))



# class LocoORM:
#
#     def __init__(self, n):
#         self.result = list(range(n))
#         self.idx = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         idx = self.idx
#         self.idx += 1
#         if self.idx > len(self.result):
#             raise StopIteration
#         return self.result[idx]
#
#
# gen = LocoORM(4)
# print(next(gen))
# print(next(gen))
# print(list(gen))


class LocoGen:

    def __init__(self, n):
        self.limit = n

    def __iter__(self):
        return self

    def __next__(self):
        i = 0
        while i < self.limit:
            yield i
            i += 1


gen = LocoGen(4)
print(next(gen))
print(next(gen))
print(list(gen))

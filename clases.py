
# class C:
#     def __init__(self, x):
#         self.x = x
#
#     def foo(self):
#         print(self.x)
#
# # c = C(2)
# # c.foo()
# # C.foo(c)
# # print(c, C)
# # print(isinstance(c, C))
# # print(type(c))
#
#
# class D(C):
#
#     def foo(self):
#         print("en d", self.x)
#         super().foo()
#
#
# d = D(5)
# d.foo()


# class C:
#     y = 77
#
#     def __init__(self, x):
#         self.x = x
#
# c1 = C(3)
# c2 = C(6)
# print(c1.x, c2.x)
# print(c1.y, c2.y)
# c1.x = 33
# print(c1.x, c2.x)
# print(c1.y, c2.y)
# C.y = 78
# print(c1.x, c2.x)
# print(c1.y, c2.y)
# c1.y = 55
# print(c1.y, c2.y)
# del c1.y
# print(c1.y, c2.y)


# class C:
#     y = 3
#     def m1(self):
#         print("m1", self)
#
#     @classmethod
#     def m2(cls):
#         print("m2", cls, cls.y)
#
#     @staticmethod
#     def m3():
#         print("m3")
#
# c = C()
# c.m1()
# c.m2()
# c.m3()

#class C:
#    def __init__(self, x):
#        self._x = x
#
#    def get_x(self):
#        return self._x
#
#    def set_x(self, valor):
#        print("==== informar")
#        self._x = valor
#
#    x = property(get_x, set_x)

#c = C(5)
#print(c.x)
#c.x = 7
#print(c.x)

# class C:
#     def __init__(self, x):
#         self._x = x
#
#     def get_x(self):
#         return self._x
#
#     x = property(get_x)
#
# c = C(5)
# print(c.x)
# c.x = 7

class C:
    def __init__(self, x):
        self._x = x
        self.__x = x

c = C(5)
print(c._x)
print(dir(c))
print(c.__x)


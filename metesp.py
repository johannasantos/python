
class C:
    def __init__(self, n):
        self.valor = list(range(n))

    def __len__(self):
        return len(self.valor)

    def __add__(self, other):
        return [x + other for x in self.valor]

    __radd__ = __add__

    def __str__(self):
        return f"<ClaseLoca {self.valor}>"

    # __new__
    # __del__

    # __getattr__
    # __setattr__
    # __getattribute__


c = C(5)
print(len(c))
print(c + 6)
print(6 + c)
print(c)
c / 5

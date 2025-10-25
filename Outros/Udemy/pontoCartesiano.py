import operator

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Ponto<{self.x}, {self.y}>"

    def __add__(self, outro):
        return Ponto(self.x + outro.x, self.y + outro.y)

    def __sub__(self, outro):
        return Ponto(self.x - outro.x, self.y - outro.y)

p1 = Ponto(1, 2)
p2 = Ponto(5, 10)

print(p1)
print(p2)
print(p1 - p2)
exit()



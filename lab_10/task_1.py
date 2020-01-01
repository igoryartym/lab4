class Arefmetic:
    def __init__(self, first, difference, n):
        self.first = first
        self.difference = difference
        self.n = n

    def progres(self):
        return self.first + self.difference * (self.n - 1)

    def sum_progres(self):
        return ((2 * self.first + self.difference * (self.n - 1)) / 2) * self.n


b = int(input("Ввести перший член арифм прогресії: "))
print(b)
c = int(input("Ввести різницю прогресії: "))
print(c)
d = int(input("Введіть який член потрібно знайти: "))
print(d)
a = Arefmetic(b, c, d)
print("Знаходження {0} члена прогресії: {1}".format(d, a.progres()))
print("Знаходження суми {0} перших членів прогресії: {1}".format(d, a.sum_progres()))

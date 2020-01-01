import datetime


class Student:
    def __init__(self, name, birthday, date, rating, scholarship_size):
        self.name = name
        self.birthday = birthday
        self.date = date
        self.rating = rating
        self.scholarship_size = scholarship_size

    def averenge(self):
        return sum(self.rating) / len(self.rating)

    def age(self):
        m = datetime.datetime.now()
        return m.year - self.birthday

    def end(self, g):
        return self.date + g


b = input("Введіть ім'я: ")
c = int(input("Введіть рік народження: "))
d = int(input("Введіть рік вступу: "))
h = int(input("Введіть скільки років залишилось навчатись: "))
j = int(input("Введіть розмір степендії: "))
t = []  # оцінки
v = [i for i in input("Ввести предмет: ").split()]
for i in v:
    n = int(input("Введіть оцінку за {0}: ".format(i)))
    t.append(n)
print(v, t)  # кінець вводу
a = Student(b, c, d, t, j)
i = a.averenge()
print("Середня арифм оцінка: {0}".format(round(i)))  # 1

for iy in range(len(t)):
    if t[iy] < i:
        print(v[iy] +": " + str(t[iy]))
print("Вік: {0}".format(a.age()))  # 3
print("В якому році ви закінчите: {0}".format(a.end(h)))  # 4

import datetime
class Person:
    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password
class reg(Person):
    def __init__(self, name, login, year_of_birth, password):
        super().__init__(name, login, password)
        self.year_of_birth = year_of_birth
        self.age = self.calculate_age()

    def calculate_age(self):
        now_y = datetime.datetime.now().year
        return now_y - self.year_of_birth


us = reg(input(), input(), int(input()), input())
us_info = {
    "Имя пользователя": us.name,
    "Логин": us.login,
    "Возраст": us.age,
    "Пароль": us.password
}
print(us_info)

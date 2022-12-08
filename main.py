import datetime as DT


def str_to_date(self_date, other_date):
    dt1 = self_date.split(".")
    dt2 = other_date.split(".")
    self_bdate = DT.date(int(dt1[2]), int(dt1[1]), int(dt1[0]))
    other_bdate = DT.date(int(dt2[2]), int(dt2[1]), int(dt2[0]))
    return self_bdate, other_bdate


class Car:
    def __init__(self, vin, number, marka, model, year_v, power, probeg, kol, cost):
        self.vin = vin
        self.number = number
        self.marka = marka
        self.model = model
        self.year_v = year_v
        self.power = power
        self.probeg = probeg
        self.kol = kol
        self.cost = cost

    # Изменяем пробег
    def set_mileage(self, km):
        self.probeg += km

    # данные об автомобиле
    def __str__(self):
        return f"Автомобиль: vin-номер:{self.vin}, гос-номер: {self.number},марка: {self.marka}," \
               f"модель: {self.model}, год выпуска: {self.year_v}, мощность: {self.power}, пробег{self.probeg} " \
               f"количество владельцев: {self.kol}, стоимость: {self.cost}"

    # Здесь и ниже операции сравнения >, >=, <, <=, ==, !=
    def __lt__(self, other):  # <
        return self.probeg < other.probeg

    def __eq__(self, other):  # ==
        return self.probeg == other.probeg

    def __le__(self, other):  # <=
        if self.__eq__(other):
            return True

        if self.__lt__(other):
            return True
        else:
            return False

    def get_age(self):
        today = DT.date.today().year
        return today - self.year_v

    def print_car(self):
        for emp in self.car:
            print(emp)


class Owner:
    def __init__(self, fio, number_ud, data, region, car_s):
        self.fio = fio
        self.number_ud = number_ud
        self.data = data
        self.region = region
        self.car_s = car_s




lada = Car('asas', 'ewe', 'sds', 'we', 2020, 89, 2323, 2, 300000)
print(lada.get_age())


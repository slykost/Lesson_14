"""ДЗ-27. Цифровой счётчик

Реализовать класс цифрового счетчика. Обеспечьте возможность установки максимального и минимального
значений, увеличения счетчика на 1, возвращения текущего значения."""

class DigitalCounter:
    def __init__(self, min, max):
        self.min_value = min
        self.max_value = max
        self.current_value = min

    def count(self):
        if self.current_value < self.max_value:
            self.current_value += 1
            return self.current_value
        else:
            return "Выходит за пределы max границы отсчета"


data = DigitalCounter(0, 10)
for _ in range(data.min_value, data.max_value + 1):
    print(data.count())
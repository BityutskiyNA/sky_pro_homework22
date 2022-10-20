# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, field, x_coord, y_coord, is_fly, crawl):
        self.field = field
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.is_fly = is_fly
        self.crawl = crawl
        self.speed = 1
        if self.is_fly and self.crawl:
            raise ValueError('Рожденный ползать летать не должен!')


    def move(self, direction):
        self.speed *= self.get_speed()
        if direction == 'UP':
            new_y = self.y_coord + self.speed
            new_x = self.x_coord
        elif direction == 'DOWN':
            new_y = self.y_coord - self.speed
            new_x = self.x_coord
        elif direction == 'LEFT':
            new_y = self.y_coord
            new_x = self.x_coord - self.speed
        elif direction == 'RIGTH':
            new_y = self.y_coord
            new_x = self.x_coord + self.speed
        self.field.set_unit(x=new_x, y=new_y, unit=self)


    def get_speed(self):
        if self.is_fly:
            return 1.2
        if self.crawl:
            return 0.5

#     ...

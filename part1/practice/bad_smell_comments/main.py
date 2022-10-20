# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    # ...
    def move_unit(self, field, x_coord, y_coord, direction, is_fly, crawl, speed = 1):
        """Функция реализует перемещение юнита по полю. в качестве параметров принимает текущие координаты юнита, 
        направление его движения, состояние не летит ли он, состояние не крадется ли он и базовый параметр скорости с 
        которым двигается юнит
        :param field: поле по которому перемещается юнит
        :param x_coord: x-координата юнита
        :param y_coord: у- координата юнита
        :param direction: направление перемещения
        :param is_fly: летит ли юнит
        :param crawl: крадется ли юнит
        :param speed: базовый параметр скорости
        """

        if is_fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed *= 1.2
            if direction == 'UP':
                new_y_coord = y_coord + speed
                new_x_coord = x_coord
            elif direction == 'DOWN':
                new_y_coord = y_coord - speed
                new_x_coord = x_coord
            elif direction == 'LEFT':
                new_y_coord = y_coord
                new_x_coord = x_coord - speed
            elif direction == 'RIGHT':
                new_y_coord = y_coord
                new_x_coord = x_coord + speed
        if crawl:
            speed *= 0.5
            if direction == 'UP':
                new_y_coord = y_coord + speed
                new_x_coord = x_coord
            elif direction == 'DOWN':
                new_y_coord = y_coord - speed
                new_x_coord = x_coord
            elif direction == 'LEFT':
                new_y_coord = y_coord
                new_x_coord = x_coord - speed
            elif direction == 'RIGHT':
                new_y_coord = y_coord
                new_x_coord = x_coord + speed

            field.set_unit(x=new_x_coord, y=new_y_coord, unit=self)

#     ...

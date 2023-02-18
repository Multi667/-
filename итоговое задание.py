class Bird:
    """Базовый класс"""

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __str__(self) -> str:
        return f'Птичка называется {self.name}. Размер составляет {self.size} м'

    def __repr__(self) -> str:
        return f'Bird(name = {self.name!r}, size = {self.size})'

    def text(self):
        return print(
            'Птицы — группа теплокровных яйцекладущих позвоночных животных, в большинстве случаев способных к полету')

    def info(self):
        return print('На данный момент не является представителем вымершего вида')


class Penguin(Bird):
    """Дочерний класс"""

    def __init__(self, name, size, speed_in_water: int):
        super().__init__(name, size)
        self.speed_in_water = speed_in_water

    # Перегрузка метода text обусловлена добавлением важной фразы, уточняющей информацию
    def text(self):
        return print(
            'Птицы — группа теплокровных яйцекладущих позвоночных животных, в большинстве случаев способных к полету. Данная птица является исключением и не способна к полету!!!')

    def info(self):
        s_info = super().info()
        return s_info

    # Перегрузка метода str обусловлена появлением нового атрибута
    def __str__(self) -> str:
        return f'Птичка называется {self.name}. Размер составляет {self.size} м. Скорость в воде {self.speed_in_water} км/ч'

    # Аналогично предыдущему пункту
    def __repr__(self) -> str:
        return f'Bird(name = {self.name!r}, size = {self.size}, speed_in_water = {self.speed_in_water})'

if __name__ == '__main__':
    bi = Penguin('Пингвин', 1, 10)
    print(bi)
    bi.text()
    bi.info()

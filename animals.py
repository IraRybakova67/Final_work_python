import argparse
import logging
from datetime import datetime

FORMAT = '{levelname:<4} - {asctime}. В модуле "{name}" ' \
         'в строке {lineno:03d} функция "{funcName}()" ' \
         'записала сообщение: {msg}'

logging.basicConfig(format=FORMAT, style='{', level=logging.INFO, filemode='a', filename='animal.log', encoding='UTF-8')
logger = logging.getLogger('animals')


class Animal:
    def __init__(self, name):
        self.name = name


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def compare(self):
        return self.wingspan


class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth

    def compare(self):
        if self.max_depth < 10:
            return "Мелководная рыба"
        elif self.max_depth > 100:
            return "Глубоководная рыба"
        else:
            return "Средневодная рыба"


class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def compare(self):
        if self.weight < 1:
            return "Малявка"
        elif self.weight > 200:
            return "Гигант"
        else:
            return "Обычный"


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args):
        if animal_type == "Bird":
            return Bird(*args)
        elif animal_type == "Fish":
            return Fish(*args)
        elif animal_type == "Mammal":
            return Mammal(*args)
        raise ValueError(f"Недопустимый тип животного: {animal_type}")



def main():
    """ Функция для запуска приложения с командной строки"""

    parser = argparse.ArgumentParser(description='Программа для  создания и описания животных')
    parser.add_argument('animal_type', choices=['Bird', 'Fish', 'Mammal'], help='Тип животного')
    parser.add_argument('name', type=str, help='Название животного')
    parser.add_argument("parameter", type=int, help="Характеристика для животного (wing span, depth, or weight)")
    args = parser.parse_args()

    try:
        animal = AnimalFactory.create_animal(args.animal_type, args.name, args.parameter)
        print(animal.compare())
        logger.info(f'{datetime.now()}: Создано  {args.animal_type}  называется {args.name}')
        print(f'Создано  {args.animal_type}  называется {args.name}')


    except ValueError:

        logger.error(f'{datetime.now()} Ошибка ввода типа животного ')
        print("Произошла ошибка, проверьте лог для дополнительной информации")


if __name__ == '__main__':
    main()

# animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
# animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
# animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)
#
# # Вывод результатов
# print(animal1.wing_length())
# print(animal2.depth())
# print(animal3.category())

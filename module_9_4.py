#lambda
from os import write

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)

#Замыкание
def  get_advanced_writer(file_name):
     def write_everything(*data_set):
         with open(file_name, 'a', encoding='utf = 8',) as f:
             for item in data_set:
                 f.write(f"{item}\n")  # Записываем каждый элемент в файл с новой строки
     return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#Метод __call__
from random import choice as ch

class MysticBall:
    def __init__(self,*words):
        self.words = words
    def __call__(self):
        return ch(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции

ВНИМАНИЕ!!: сдача задания
1) создать папку Lesson_1_Ivanov
2) в папку положить файлы task_1 - task_6 (а также txt-файл для последнего)
3) заархивировать папку! и сдать архив

Все другие варианты сдачи приму только один раз, потом буду ставить НЕ СДАНО
"""
text_1, text_2, text_3 = "разработка", "сокет", "декоратор"

print(type(text_1),"\t", type(text_2),"\t", type(text_3))
print(text_1,"\t", text_2,"\t\t", text_3)

text_1 = "\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430"
text_2 = "\u0441\u043e\u043a\u0435\u0442"
text_3 = "\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440"

print(type(text_1),"\t", type(text_2),"\t", type(text_3))
print(text_1,"\t", text_2,"\t\t", text_3)
from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date
import emoji


if __name__ == '__main__':
    calculate_salary(10) # если импортируем полностью модуль то название модуля.объект
    get_employees('Oleg')
    print(date.today())
    emoji.print_simbol(question=input('Тебе нравится Python? Введи: "Да", "Нет":'))
    
    # найти интересный пакет в requirements указать его версию,
    # при желании написать программу с этим пакетом


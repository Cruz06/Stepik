from datetime import datetime, timedelta
from random import randrange, randint

from dateutil.relativedelta import relativedelta
from faker import Faker

# функция, которая будет генерировать разное число для ввода в поле ввода даты
# рождения в формате 'дд.мм.гггг', но с условием что возраст будет от 18 до 55 лет.

# взять текущее время - отнять 55 лет
# взять текущее время - отнять 18 лет
# в этих пределах рандномно выбрать число и превратить в dd.mm.yyyyy

# генерировать номера телефонов, чтобы был формат  на выходе например 905243аабб,
# ( 905243 это не меняется в номере) где  я б мог выбирать диапазон нужных чисел
# в 'аа', затем в 'бб'. Нужно вывести полученные номера в столбик для копирования,
# а затем их вставить в массив для последующих манипуляций с данными номерами.
# Механика работы- я задаю параметр для аа например от 01 до 50, получаю 50 номеров,
# почему надо в столбец выводить- чтобы я их мог скопировать  и вставить в Эксель
# ( это обязательное условие). Затем эти полученные 50 номеров вставить как данные
# для выполнения автотестов- 50 штук. Или если легче, то можно рандомные номера, но
# начинающиеся с 9 длина 10 знаков с возможностью выбора количества генерированных
# номеров , остальные условия теже.

fake_date = Faker().date_between(start_date='-55y', end_date='-18y')
print("faker random date is", fake_date.strftime("%d %m %Y"))

print(f"---\n>>>now is {datetime.now()} - 1 year = ", (datetime.now() - relativedelta(years=1)))

lo = (datetime.now() - relativedelta(years=55))
hi = (datetime.now() - relativedelta(years=18))
print("---\ninterval between lowest date %s and highest %s\nthere are %s days between them\nrandom picked date is %s" %
      (lo, hi, (hi - lo).days, (lo + timedelta(days=randrange((hi - lo).days))).strftime("%d %m %Y")))


def get_numbers(how_many, aa, bb):
    return [f"905243{randint(min(aa), max(aa)):02}{randint(min(bb), max(bb)):02}" for _ in range(how_many)]


def get_random_numbers(how_many):
    return [f"9{randint(0, 999999999):09}" for _ in range(how_many)]


lst = get_numbers(10, aa=[99, 16], bb=[0, 1])
print(*lst, sep="\n")
print(lst)

print("---")

lst_one = get_random_numbers(10)
print(*lst, sep="\n")
print(lst)
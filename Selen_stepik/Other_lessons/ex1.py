# def get_list():
#     for x in [1, 2, 3, 4]:
#         yield x


# a = get_list()
# for x in a:
#     print(x)

# среднеарифметическое убывающего списка чисел
# def get_gen_list():
#     for i in range(1, 10):
#         a = range(i, 11)
#         yield sum(a) / len(a)
#
#
# a = get_gen_list()
# print(list(a))
import math
def solve_quiz_and_get_code(self):
    alert = self.browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    print(x)
    print(answer)


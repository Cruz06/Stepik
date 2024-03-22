# def get_list():
#     for x in [1, 2, 3, 4]:
#         yield x


# a = get_list()
# for x in a:
#     print(x)

# среднеарифметическое убывающего списка чисел
def get_gen_list():
    for i in range(1, 10):
        a = range(i, 11)
        yield sum(a) / len(a)


a = get_gen_list()
print(list(a))


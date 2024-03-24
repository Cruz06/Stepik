# найти все вхождения слова "генератор" в файле lesson54
def find_word(f, word):
    g_index = 0
    for line in f:
        current_index = 0
        while current_index != -1:
            current_index = line.find(word, current_index)
            if current_index > - 1:
                yield g_index + current_index
                current_index += 1
        g_index += len(line)


try:
    with open("lesson54.txt", encoding="utf-8") as file:
        a = find_word(file, "генератор")
        print(list(a))
except FileNotFoundError:
    print("Файл не найден")
except:
    print("Ошибка обработки файла")

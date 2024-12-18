def count_letter(str):
    str_low = str.lower() #перенос всех заглавных букв в строчные
    dict = {} #создание пустого словаря

    for i in str_low: #перебор всех элементов строки с присваиванием каждого в i
        if i.isalpha(): #проверка на буквенность элемента
            if i not in dict:
                dict[i] = 1 #добавление элемента в словарь при его отутствии там
            else:
                dict[i] += 1 #увелечение значения при повторе
    return dict #возвращение словаря
# TODO  Напишите функцию count_letters

def calculate_frequency(dict2):
    a = 0

    for i in dict2:
        a = a + dict2[i] #найдём кол-во используемых символов, пробежавшись по всему словарю

    for i in dict2:
        dict2[i] = dict2[i] / a #проходимся по всем элементам словаря и заменяем значения у ключей на частатоту
    return dict2 #возвращаем обновлённый словарь
# TODO Напишите функцию calculate_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

for key, value in calculate_frequency(count_letter(main_str)).items():
    print(f"{key}:", format(value, '.2f'))

# TODO Распечатайте в столбик букву и её частоту в тексте

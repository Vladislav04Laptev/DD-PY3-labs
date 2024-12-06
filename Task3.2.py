# TODO Напишите функцию find_common_participants
def find_common_participants(f_group, s_group, point = ","):
     f_list = f_group.split(point)
     s_list = s_group.split(point) #перевод строк первой и второй группы в списки с разделителем |

     res = [] #список с общими участниками
     for i in f_list: #перебор участников первой группы
         if i in s_list: #проверка наличия учатсника первой группы во второй
             res.append(i) #добавление в список общих учатсников

     res.sort() #сортировка участников
     return res #возвращение списка общих учатсников

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

find_common_participants(participants_first_group, participants_second_group, "|")
# TODO Провеьте работу функции с разделителем отличным от запятой

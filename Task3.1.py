# TODO Напишите функцию для поиска индекса товара
def f_find_index_item (product_list, item_name):
    for i in range(len(product_list)): #перебор всех элементов списка, переданного в функцию
        if (product_list[i] == item_name): #сравнение каждого элемента с искомым
            return i #возвращение номера первого вхождения товара
    return None #возвращение None при отсутствии товара в списке

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = f_find_index_item(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

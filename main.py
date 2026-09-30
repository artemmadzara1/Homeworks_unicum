import ctypes

class CommonList:
    def __init__(self):
        self._length = 0
        self._capacity = 1
        self._array = self.make_array(self._capacity)

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        if not 0 <= index < self._length:
            raise IndexError("Out of range")
        return self._array[index]

    def append_to_common_list(self,item):
        if self._length == self._capacity:
            self._resize(2*self._capacity)

        self._array[self._length] = item
        self._length += 1

    def _resize(self,new_capacity):
        #создание нового списка
        new_array = self.make_array(new_capacity)
        #Копирование старых элементов в новый список
        for i in range(self._length):
            new_array[i] = self._array[i]

        self._array = new_array
        self._capacity = new_capacity

    def make_array(self, capacity):

        return (capacity * ctypes.py_object)()

    def __repr__(self):
        items = [str(self._array[i]) for i in range(self._length)]
        return "#" + ' & '.join(items) + "#"

#наша коллекция
my_common_list = CommonList()
# my_common_list.append_to_common_list("Hi dady")
# my_common_list.append_to_common_list("Hi momy")
# print(iter(my_common_list))
# print(id(my_common_list))
# my_common_list.append_to_common_list("Hi dady")
# print(id(my_common_list)) ячейка пямяти не меняеться
#список python
# my_mini_lst =["Hi dady","Hi momy"]
# print(iter(my_mini_lst))
# print(id(my_mini_lst))
# my_mini_lst.append("Hi dady")
# print(id(my_mini_lst)) список точнее ячейка памяти не изменяеться
print("Вывод: в колекции которую мы написали сами выводит Iter:<iterator object at 0x000001E94263FC70> а ID:2101352733664\n"
     "в списке котрорый нам даеться от python Iter:<list_iterator object at 0x000001E9423405E0> а ID:2101349824320.\n"
     "Пояснение почему разные итератоы, они разные потомучто когда мы писали мы нигде не упоминали что это список и тоесть мы сами написали такие же способы как у списка но без\n"
     "упоминания списка.\n"
     "при добавление в колекцию и список новый элемент ячейка памяти не меняеться.\n"
     "получаеться что наша колекция слишком схожа со списком.\n"
     "функционал почти одинаковой с нашей колекцией только у них разное выполнение действий, к нашей колекции\n"
      "нельзя применять методы python")
#доказательство
# my_common_list.append(34)
# print(my_common_list) AttributeError: 'CommonList' object has no attribute 'append' ошибка

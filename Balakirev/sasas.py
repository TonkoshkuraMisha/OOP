class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    def get_data(self):
        return self.__data

    def set_prev(self, obj):
        self.__prev = obj

    def get_prev(self):
        return self.__prev

    def set_next(self, obj):
        self.__next = obj

    def get_next(self):
        return self.__next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.tail is None:  # Если список пустой
            self.head = self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self, indx):
        if indx < 0:
            return
        current = self.head
        count = 0
        while current is not None and count < indx:
            current = current.get_next()
            count += 1
        if current is None:
            return
        if current.get_prev() is None:  # удаляем первый элемент
            self.head = current.get_next()
            if self.head:
                self.head.set_prev(None)
        else:
            current.get_prev().set_next(current.get_next())
        if current.get_next() is None:  # удаляем последний элемент
            self.tail = current.get_prev()
            if self.tail:
                self.tail.set_next(None)
        else:
            current.get_next().set_prev(current.get_prev())

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def __call__(self, indx):
        if indx < 0:
            raise IndexError("индекс вне диапазона")
        current = self.head
        count = 0
        while current is not None and count < indx:
            current = current.get_next()
            count += 1
        if current is None:
            raise IndexError("индекс вне диапазона")
        return current.get_data()

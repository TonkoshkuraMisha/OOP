class Message:
    def __init__(self, text):
        self.text = text
        self.fl_like = False  # Изначально лайк не установлен


class Viber:
    def __init__(self):
        self.messages = []  # Инициализируем список сообщений

    def add_message(self, msg):
        """Добавление нового сообщения в список сообщений."""
        self.messages.append(msg)

    def remove_message(self, msg):
        """Удаление сообщения из списка."""
        if msg in self.messages:
            self.messages.remove(msg)

    def set_like(self, msg):
        """Поставить/убрать лайк для сообщения msg."""
        for message in self.messages:
            if message == msg:
                message.fl_like = not message.fl_like  # Инвертируем значение fl_like
                break

    def show_last_messages(self, number):
        """Отображение последних сообщений."""
        if number <= 0:
            print("Число должно быть положительным.")
            return
        num_messages = min(number, len(self.messages))
        last_messages = self.messages[-num_messages:]
        for message in last_messages:
            print(message.text)

    def total_messages(self):
        """Возвращает общее число сообщений."""
        return len(self.messages)


# Пример использования классов

# Создаем экземпляр класса Viber
viber = Viber()

# Создаем сообщения
msg1 = Message("Всем привет!")
msg2 = Message("Это курс по Python ООП.")
msg3 = Message("Что вы о нем думаете?")

# Добавляем сообщения в мессенджер (используем экземпляр viber, а не класс Viber)
viber.add_message(msg1)
viber.add_message(msg2)
viber.add_message(msg3)

# Поставляем лайк первому сообщению
viber.set_like(msg1)

# Удаляем второе сообщение
viber.remove_message(msg2)

# Отображаем последние 2 сообщения
viber.show_last_messages(2)

# Выводим общее количество сообщений
print("Общее количество сообщений:", viber.total_messages())

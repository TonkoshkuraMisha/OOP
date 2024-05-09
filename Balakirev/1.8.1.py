class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


class Server:
    def __init__(self):
        import random
        self.ip = random.randint(1, 1000)  # Генерируем случайный IP-адрес
        self.buffer = []  # Список принятых пакетов

    def send_data(self, data):
        # Отправляем пакет данных роутеру
        router.receive_data(data)

    def get_data(self):
        # Возвращаем список принятых пакетов и очищаем буфер
        data = self.buffer
        self.buffer = []
        return data

    def get_ip(self):
        # Возвращает IP-адрес сервера
        return self.ip


class Router:
    def __init__(self):
        self.servers = []  # Список подключенных серверов
        self.buffer = []  # Буфер для принятых пакетов

    def link(self, server):
        # Присоединяем сервер к роутеру
        self.servers.append(server)

    def unlink(self, server):
        # Отсоединяем сервер от роутера
        if server in self.servers:
            self.servers.remove(server)

    def receive_data(self, data):
        # Принимаем данные от сервера и сохраняем в буфере
        self.buffer.append(data)

    def send_data(self):
        # Отправляем все пакеты из буфера соответствующим серверам
        for data in self.buffer:
            for server in self.servers:
                if server.get_ip() == data.ip:
                    server.buffer.append(data)
        self.buffer = []  # Очищаем буфер после отправки


# Пример использования классов

# Создаем объекты
router = Router()
sv_from = Server()
sv_from2 = Server()
sv_to = Server()

# Подключаем серверы к роутеру
router.link(sv_from)
router.link(sv_from2)
router.link(sv_to)

# Отправляем данные от сервера sv_from к серверу sv_to
data1 = Data("Hello", sv_to.get_ip())
sv_from.send_data(data1)

# Отправляем данные от сервера sv_from2 к серверу sv_to
data2 = Data("Hi", sv_to.get_ip())
sv_from2.send_data(data2)

# Отправляем данные от сервера sv_to к серверу sv_from
data3 = Data("Response", sv_from.get_ip())
sv_to.send_data(data3)

# Роутер отправляет все накопленные данные
router.send_data()

# Получаем данные с серверов
msg_lst_from = sv_from.get_data()
msg_lst_from2 = sv_from2.get_data()
msg_lst_to = sv_to.get_data()

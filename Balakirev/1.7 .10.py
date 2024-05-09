class Application:
    def __init__(self, name):
        self.name = name
        self.blocked = False  # По умолчанию приложение не заблокировано


class AppStore:
    def __init__(self):
        self.applications = []  # Список приложений в магазине

    def add_application(self, app):
        self.applications.append(app)

    def remove_application(self, app):
        if app in self.applications:
            self.applications.remove(app)

    def block_application(self, app):
        for application in self.applications:
            if application == app:
                application.blocked = True

    def total_apps(self):
        return len(self.applications)

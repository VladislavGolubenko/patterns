class ProjectManager:

    def find_order(self):
        print('I\'m find order')

    def create_tz(self):
        print('I\'m create tz')

    def control(self):
        print('I\'m control project')


class Recruter:

    def find_programmer(self):
        print('I\'m find programmer')


class Programmer:

    def write_code(self):
        print('I\'m write code')

    def think(self):
        print('I\'m think')


class Facade:
    def __init__(self):
        self.project_manager = ProjectManager()
        self.recruter = Recruter()
        self.programmer = Programmer()

    def itog(self):
        for i in range(6):
            self.project_manager.create_tz()

        for i in range(12):
            self.programmer.think()

        for i in range(345):
            self.programmer.write_code()

        for i in range(5):
            self.project_manager.control()


if __name__ == '__main__':
    facade = Facade()
    facade.itog()

class OS:
    def show_change(self, change):
        raise NotImplementedError


class IOS(OS):
    def say_what_new(self, change):
        print(f'В вашей версии IOS присутствуют изменения: {change}')


class Android(OS):
    def say_what_new(self, change):
        print(f'В вашей версии Android присутствуют изменения: {change}')


class PresentationBase:
    def __init__(self):
        self._os = self.get_os()

    def get_os(self):
        raise NotImplementedError

    def compare_versions(self, change):
        self._os.say_what_new(change)


class PresentationOfAndroid(PresentationBase):

    def __init__(self):
        super().__init__()
        self._memory = []

    def get_os(self):
        return Android()

    def compare_versions(self, change):
        super().compare_versions(change)
        self._memory.append(change)

    def say_total(self):
        print(f"\n За все время реализовано: {'; '.join(self._memory)}")


if __name__ == '__main__':
    presentation = PresentationOfAndroid()
    presentation.compare_versions('добавили виджеты')
    print('-'*12, 'на следующей презентации')
    presentation.compare_versions('добавили всплывающие окна')
    presentation.say_total()

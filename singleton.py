class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):

    def get_logic(self):
        ...


if __name__ == "__main__":
    sing1 = Singleton()
    sing2 = Singleton()

    print(sing1.__dict__)

    if id(sing1) == id(sing2):
        print('Все работает коррректно, id двух классов синглтона равны')
    else:
        print('Что-то пошло не по плану')
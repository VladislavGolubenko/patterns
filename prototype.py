import copy


class SelfReferencing:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class ObjectToCopy:
    def __init__(self, some_int, some_list, some_circular_ref):
        self.some_int = some_int
        self.some_list = some_list
        self.some_circular_ref = some_circular_ref

    def __copy__(self):

        some_list = copy.copy(self.some_list)
        some_circular_ref = copy.copy(self.some_circular_ref)

        new = self.__class__(
            self.some_int, some_list, some_circular_ref
        )
        new.__dict__.update(self.__dict__)
        return new

    def __deepcopy__(self, memo=None):

        if memo is None:
            memo = {}

        some_list = copy.deepcopy(self.some_list, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        new = self.__class__(
            self.some_int, some_list, some_circular_ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new

    def method_objecttocopy(self):
        return "это наш метод класса ObjectToCopy"


if __name__ == "__main__":

    circular_ref = SelfReferencing()
    list_values = [2, 6, 8]
    object = ObjectToCopy(23, list_values, circular_ref)
    still_object = object

    print('-' * 20, 'Неглубокое копирование', '-' * 20)

    copy_object = copy.copy(object)
    object.some_list.append(10)

    print(object.__dict__)
    print(copy_object.__dict__)

    print('-' * 20, 'Глубокое копирование', '-' * 20)

    deep_copy_object = copy.deepcopy(object)
    object.some_list.append(12)

    print(object.__dict__)
    print(deep_copy_object.__dict__)

    print('-' * 20, 'ID ячеек памяти', '-' * 20)

    print('object: ', id(object))
    print('still: ', id(still_object))
    print('object_copy: ', id(copy_object))
    print('object_copy_deep: ', id(deep_copy_object))

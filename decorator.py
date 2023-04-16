def my_decorator(argument):
    def real_decorator(function):
        def wraper_function():
            print(f'before{argument}')
            function()
            print('after')
        return wraper_function
    return real_decorator


@my_decorator(1)
def some_function():
    print('go inside')
    print('qwerty')

some_function()
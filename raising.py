class ShortInputException(Exception):
    '''Пользовательскй класс исключения'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Введите чо нить >')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)

except EOFError:
    print('Ну и зач ты эт сделал ?')
except ShortInputException as ex:
    print('ShortInputException: Длинна введённой строки -- {0}; \
    ожидалось, как минимум, {1}'.format(ex.length, ex.atleast))
else:
    print('Не было исключений')
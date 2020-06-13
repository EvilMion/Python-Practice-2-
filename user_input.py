def reverse(str):
    return str[::-1]

def is_palidrome(str):
    return str == reverse(str)

something = input('Введите текст: ')
if (is_palidrome(something)):
    print("Да, это палидром")
else:
    print("нЕт, эТо Не ПаЛиДрОм")
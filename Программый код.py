# Определяем класс с именем Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Определяем класс с именем Stack
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0


    # Функция добавления элемента в стек
    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1
        print('ok: элемент успешно добавлен в стек')


    # Функция удаления и возврата последнего элемента из стека
    def pop(self):
        if self.head is None:
            print('error: стек пуст')
        else:
            print('Значение удаляемого элемента: ', self.head.value)
            self.head = self.head.next
            self.size -= 1


    # Функция возврата последнего элемента из стека, не удаляя его
    def back(self):
        if self.head is None:
            print('error: стек пуст')
        else:
            print('Последний элемент стека: ', self.head.value)


    # Функция, возвращающая количество элементов в стеке
    def get_size(self):
        print('Размер стека: ', self.size)


    # Функция очистки стека
    def clear(self):
        self.head = None
        self.size = 0
        print('ok: стек успешно очищен')


# Определит функцию для печати меню
def print_menu():
    print("\nДобро пожаловать в программу стека!")
    print("\nМеню команд:")
    print("push <n> - добавить в стек число n")
    print("pop - удалить из стека последний элемент")
    print("back - вывести значение последнего элемента в стеке")
    print("size - вывести количество элементов в стеке")
    print("clear - очистить стек")
    print("exit - завершить работу")
    print("\nКоманда:")


# Создает экземпляр класса Stack
stack = Stack()


# Распечатает меню
print_menu()


# Вводим цикл, чтобы непрерывно принимать вводимые пользователем данные и выполнять соответствующие операции
while True:
    command = input().split() # Возьмёт пользовательский ввод и разделит его на список слов
    if command[0] == 'push': # Проверит, является ли первое слово команды «push»

        # Проверит, равна ли длина команды 2-м (т.е. содержит ли она число для ввода)
        if len(command) != 2:

            # Выведет «ошибку», если команда недействительна
            print("error: команда должна быть в формате 'push <n>'")
        else:

            # Попробует преобразовать второе слово команды в целое число и поместить его в стек
            try:
                stack.push(int(command[1]))

            # Выведет «ошибку», если второе слово команды не может быть преобразовано в целое число
            except ValueError:
                print("error: значение должно быть целым числом")

    # Проверит, является ли первое слово команды «pop»
    elif command[0] == 'pop':
        stack.pop()

    # Проверит, является ли первое слово команды «back»
    elif command[0] == 'back':
        stack.back()

    # Проверит, является ли первое слово команды «size»
    elif command[0] == 'size':
        stack.get_size()

    # Проверит, является ли первое слово команды «clear»
    elif command[0] == 'clear':
        stack.clear()

    # Проверит, является ли первое слово команды «exit»
    elif command[0] == 'exit':
        print("bye")
        break

    else:

        # Выведет «ошибку», если команда не распознана
        print("error: неизвестная команда, пожалуйста, введите команду из меню команд!")
        print_menu()
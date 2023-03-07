import csv


class Products_in_the_store:
    # Скидка!
    price_level = 0.85
    # Создает список(хранит экземпляры класса)
    list_product_in_the_store = []
    # Флаг, обнуление списка, на случай если в существующий список товаров не нужно добавлять товары из файла
    clear_list = True


    def __init__(self, product_name: str = "безымянный", product_price: int = 0, product_quantity: int = 0):
        """
        Инициализация класса
        :param product_name: название товара
        :param product_price: цена товара
        :param product_quantity: количество товара
        """
        self.__product_name = product_name
        self.product_price = product_price
        self.product_quantity = product_quantity
        Products_in_the_store.list_product_in_the_store.append(self)


    @classmethod
    def read_csv(cls):
        """
        Считывает товар, его характеристики и записывает экземпляр в список
        Если флаг clear_list == True, обнуляет список, иначе дописывает в существующий
        :return:
        """
        if cls.clear_list:
            cls.list_product_in_the_store = []
        with open('data\items.csv') as file:
            line_list = csv.DictReader(file)
            for row in line_list:
                cls(row['name'], row['price'], row['quantity'])


    @property
    def product_name(self) -> str:
        """
        Преобразование обращения к методу как к переменной. Открываем доступ к переменной __product_name
        :return:
        """
        return self.__product_name


    @product_name.setter
    def product_name(self, name: str):
        """
        Проверка длины названия продукта (<= 10 символов)
        :param name: Новое имя продукта
        """
        if len(name) < 11:
            self.__product_name = name
        else:
            print("Exception: Длина наименования товара превышает 10 символов.")


    def total_cost_of_the_product(self) -> int:
        """
        Общая стоимость, данной категории товара
        :return: Возвращает общую стоимость товара = цена одного товара * количество данного товара
        """
        total_cost_product = self.product_price * self.product_quantity
        return total_cost_product


    def apply_discount(self):
        """
        Применяет скидку к данной категории товара
        :return: Возвращает стоимость товара, с примененной скидкой
        """
        self.product_price = self.product_price * self.price_level
        return self.product_price


    @staticmethod
    def is_integer(number=None) -> bool:
        """
        Проверка числа на целое число
        :param number: число для проверки
        :return: Возврат True если целое, False если не целое
        """
        # Проверка введенных данных
        if number == None:
            return "is_integer(сюда нужно ввести число)"

        # Проверка числа на тип int
        if isinstance(number, int):
            return True

        # Проверка числа на тип int, если число представлено в виде float
        number = str(number)
        number = number.split('.')
        if number[1] == '0':
            return True

        return False


    def __repr__(self) -> str:
        """
        :return: Возврат названия класса и переменныых поступивших при инициализации
        """
        return f"Products_in_the_store({self.__product_name}, {self.product_price}, {self.product_quantity})"


    def __str__(self) -> str:
        """
        :return: Возврат названия товара
        """
        return self.__product_name


class Phone(Products_in_the_store):
    def __init__(self, product_name: str, product_price: int, product_quantity: int, number_of_sim: int = 0):
        """
        Модернизация класса Products_in_the_store, добавляет кол-во сим-карт
        :param product_name: Наследие от Products_in_the_store
        :param product_price: Наследие от Products_in_the_store
        :param product_quantity: Наследие от Products_in_the_store
        :param number_of_sim: Количество поддерживаемых сим-карт
        """
        super().__init__(product_name, product_price, product_quantity)
        self.number_of_sim = number_of_sim


    def __add__(self, other: object) -> int:
        """
        Сложение количества товаров класса Phone и Products_in_the_store
        :param other: Класс Products_in_the_store
        :return: Сумма количества товаров
        """
        if isinstance(other, Products_in_the_store):
            return other.product_quantity + self.product_quantity
        else:
            return "Только с классом Products_in_the_store"


class MixinLanguage:
    """ Словарик для реализации смены языка"""
    language_dict: dict = {'EN': 'RU', 'RU': 'EN'}


    def __init__(self, *args):
        """
        Создаем переменную с установленой раскладкой
        :param args: Передаем полученные параметры в следующий init
        """
        self.__language: str = 'EN'
        super().__init__(*args)


    def change_lang(self) -> str:
        """
        Метод меняющий раскладку, каждый вызов меняет на противоположную
        :return: Возврат измененой раскладки
        """
        self.__language: str = self.language_dict[self.__language]
        return self.__language


    @property
    def language(self) -> str:
        return self.__language


class KeyBoard(MixinLanguage, Products_in_the_store):
    def __init__(self, *args):
        """
        Получает и передает параметры в следующий init
        :param args:
        """
        super().__init__(*args)

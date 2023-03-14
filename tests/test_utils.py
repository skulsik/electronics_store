from utils.utils import *
import pytest


class Test_Products_in_the_store():
    # Создаем экземпляр для теста
    products_in_the_store = Products_in_the_store()


    def test_read_csv_not_file(self):
        """Проверка на вывод ошибки отсутствует фаил"""
        Products_in_the_store.path_file = 'items.csv'
        assert Products_in_the_store.read_csv() == 'FileNotFoundError: Отсутствует файл item.csv'


    def test_read_csv_no_name(self):
        """Проверка на вывод ошибки нет ключа name"""
        Products_in_the_store.path_file = '..\data\items_no_name.csv'
        assert str(Products_in_the_store.read_csv()) == 'ReadCSVErrorName: Отсутствует ключ name'


    def test_read_csv_no_price(self):
        """Проверка на вывод ошибки нет ключа price"""
        Products_in_the_store.path_file = '..\data\items_no_price.csv'
        assert str(Products_in_the_store.read_csv()) == 'ReadCSVErrorName: Отсутствует ключ price'


    def test_read_csv_no_quantity(self):
        """Проверка на вывод ошибки нет ключа quantity"""
        Products_in_the_store.path_file = '..\data\items_no_quantity.csv'
        assert str(Products_in_the_store.read_csv()) == 'ReadCSVErrorName: Отсутствует ключ quantity'


    def test_total_cost_of_the_product_none(self):
        """
        Проверка без введенных данных
        :return:
        """
        assert self.products_in_the_store.total_cost_of_the_product() == 0


    def test_total_cost_of_the_product(self):
        """
        Проверяем с введенными данными
        :return:
        """
        self.products_in_the_store.product_price = 23000
        self.products_in_the_store.product_quantity = 18
        assert self.products_in_the_store.total_cost_of_the_product() == 414000
        assert self.products_in_the_store.product_name == "безымянный"


    def test_apply_discount_no(self):
        """
        Применение старой скидки
        :return:
        """
        self.products_in_the_store.product_price = 23000
        assert self.products_in_the_store.apply_discount() == 19550


    def test_apply_discount_yes(self):
        """
        Применение новой скидки
        :return:
        """
        self.products_in_the_store.product_price = 23000
        self.products_in_the_store.price_level = 0.5
        assert self.products_in_the_store.apply_discount() == 11500


    def test_product_name(self):
        """
        Проверка на введение корректных данных
        :return:
        """
        item = Products_in_the_store("Фен", 1_000_000, 1)
        item.product_name = "Мотоцикл"
        assert item.product_name == "Мотоцикл"


    def test_product_name_more(self):
        """
        Проверка слова, длинна которого больше 10 символов
        :return:
        """
        item = Products_in_the_store("Фен", 1_000_000, 1)
        item.product_name = "Вибромасажер"
        assert item.product_name == "Фен"


    def test_is_integer_int(self):
        """
        Ввод целого числа
        :return:
        """
        assert Products_in_the_store.is_integer(777) == True


    def test_is_integer_int_float(self):
        """
        Ввод целого числа в формате float
        :return:
        """
        assert Products_in_the_store.is_integer(9.0) == True


    def test_is_integer_false(self):
        """
        Ввод не целого числа
        :return:
        """
        assert Products_in_the_store.is_integer(9.9) == False


    def test_is_integer_error(self):
        """
        Ни чего не вводим, проверка на ошибку
        :return:
        """
        assert Products_in_the_store.is_integer() == 'is_integer(сюда нужно ввести число)'


class Test_Phone():
    # Создаем экземпляр для теста
    product1 = Phone("nokia", 20_000, 2)
    product2 = Products_in_the_store("doogee", 3_000, 4)


    def test__init__(self):
        """
        Проверка без введенных данных
        :return:
        """
        assert self.product1.number_of_sim == 0

    def test__add__(self):
        """
        Проверка сложения классов в отношениях
        :return:
        """
        assert (self.product1 + self.product2) == 6


    def test__add__error(self):
        """
        Проверка сложения классов в отношениях
        :return:
        """
        assert (self.product1 + 7898) == "Только с классом Products_in_the_store"


class Test_KeyBoard():
    # Создаем экземпляр для теста
    product = KeyBoard('Dark Project KD87A', 9600, 5)


    def test__language(self):
        """
        Проверка на предворительно заданные данные
        :return:
        """
        assert self.product.language == "EN"


    def test_change_lang(self):
        """
        Проверка на смену раскладки, после вызова метода
        :return:
        """
        assert self.product.change_lang() == "RU"
        assert self.product.change_lang() == "EN"
        assert self.product.change_lang() == "RU"

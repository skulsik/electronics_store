from utils.utils import Products_in_the_store


class Test_Products_in_the_store():
    # Создаем экземпляр для теста
    products_in_the_store = Products_in_the_store()


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

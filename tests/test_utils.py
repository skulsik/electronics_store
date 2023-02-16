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
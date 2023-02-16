class Products_in_the_store:
    # Скидка!
    price_level = 0.85
    # Создает список(хранит экземпляры класса)
    list_product_in_the_store = []


    def __new__(cls, *args, **kwargs):
        """
        Создает экземпляр данного класса и добавляет его в список
        :param args:
        :param kwargs:
        """
        cls.list_product_in_the_store.append(super().__new__(cls))
        return super().__new__(cls)


    def __init__(self, product_name="безымянный", product_price=0, product_quantity=0):
        """
        Инициализация класса
        :param product_name: название товара
        :param product_price: цена товара
        :param product_quantity: количество товара
        """
        self.product_name = product_name
        self.product_price = product_price
        self.product_quantity = product_quantity


    def total_cost_of_the_product(self):
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

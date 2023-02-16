from utils.utils import Products_in_the_store


item1 = Products_in_the_store("Смартфон", 10000, 20)
item2 = Products_in_the_store("Ноутбук", 20000, 5)

print(item1.total_cost_of_the_product())
print(item2.total_cost_of_the_product())


Products_in_the_store.price_level = 0.8  # устанавливаем новый уровень цен
item1.apply_discount()
print(item1.product_price)
print(item2.product_price)

print(Products_in_the_store.list_product_in_the_store)

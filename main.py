from utils.utils import Products_in_the_store

# ТЗ-1
# item1 = Products_in_the_store("Смартфон", 10_000, 20)
# item2 = Products_in_the_store("Ноутбук", 20_000, 5)
#
# print(item1.total_cost_of_the_product())
# print(item2.total_cost_of_the_product())
#
# Products_in_the_store.price_level = 0.8  # устанавливаем новый уровень цен
# item1.apply_discount()
#
# print(item1.product_price)
# print(item2.product_price)
# print(Products_in_the_store.list_product_in_the_store)


# ТЗ-2
item1 = Products_in_the_store("Laptop", 54_000, 3)
print(item1.product_name)

item1.product_name = "Вибромасажёр"
print(item1.product_name)

item1.product_name = "Чайник"
print(item1.product_name)

Products_in_the_store.read_csv()
print(len(Products_in_the_store.list_product_in_the_store))

item2 = Products_in_the_store.list_product_in_the_store[0]
print(item2.product_name)

print(Products_in_the_store.is_integer(5))
print(Products_in_the_store.is_integer(5.0))
print(Products_in_the_store.is_integer(5.5))
print(Products_in_the_store.is_integer())

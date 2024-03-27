#Дополнительное задание

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента.")
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте.")

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена на товар '{item_name}' обновлена.")
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте.")


store1 = Store("Магазин фруктов", "ул. Первомайская, 10")
store2 = Store("Супермаркет 'Полезные продукты'", "пр. Ленина, 25")
store3 = Store("Магазин электроники", "ул. Гагарина, 5")

store1.add_item("Яблоки", 100)
store1.add_item("Бананы", 150)
store1.add_item("Апельсины", 120)

store2.add_item("Молоко", 90)
store2.add_item("Хлеб", 50)
store2.add_item("Яйца", 150)

store3.add_item("Ноутбук", 30000)
store3.add_item("Смартфон", 20000)
store3.add_item("Наушники", 5000)

# Тестирование методов
print("\nТестирование магазина 'Магазин фруктов':")
print("Цена на яблоки:", store1.get_price("Яблоки"))
store1.update_price("Яблоки", 110)
print("Цена на яблоки после обновления:", store1.get_price("Яблоки"))
store1.remove_item("Бананы")
store1.remove_item("Киви")

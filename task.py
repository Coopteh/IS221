class  Product:
    def __init__(self, name, price):
        self .name = name
        self .price = price

    def print_label(self):
        print(f"Продукт {self.name} цена {self.price}")

class Pizza(Product):
    def __init__(self, name, price):
        super().__init__(name, price)

class Milk(Product):
    def __init__(self, name, price, color):
        self.__color = color
        super().__init__(name, price)

    def print_label(self):
        print(f"Продукт {self.name} цена {self.price} цвет {self.__color}")

obj_pizza = Pizza("пицца", 500)
obj_milk = Milk("молоко", 76, "белый")
obj_pizza.print_label()
obj_milk.print_label()

class Restaurante():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("O " + self.restaurant_name + " trabalha com o tipo de cozinha " + self.cuisine_type)

    def open_restaurant(self):
        print("O " + self.restaurant_name + " está Aberto!")

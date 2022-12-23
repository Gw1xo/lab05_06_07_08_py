class Shop:

    def __init__(self, shop_name, shop_type):
        self.shop_name = shop_name
        self.shop_type = shop_type
        self.number_of_units = 0

    def describe_shop(self):
        return f'Shop name: {self.shop_name}\nShop type: {self.shop_type}'

    def open_shop(self):
        return f"Shop {self.shop_name} open!"

    def set_number_units(self, num):
        self.number_of_units = num

    def increment_number_of_units(self, num):
        self.number_of_units += num


class Discount(Shop):
    def __init__(self, shop_name, shop_type, *discount_product):
        self.discount_products = discount_product[:]
        super().__init__(shop_name, shop_type)

    def get_discount_products(self):
        return self.discount_products

    
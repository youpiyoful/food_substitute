"""This file contain the food object than map table food"""


class Food:
    """Representation of food entity"""

    def __init__(self, id_food, product_name,
                 generic_name, stores_tags, url, nutrigrade, id_category):
        """Initialize"""
        self.id_food = id_food
        self.product_name = product_name
        self.generic_name = generic_name
        self.stores_tags = stores_tags
        self.url = url
        self.nutrigrade = nutrigrade
        self._id_category = id_category

    @staticmethod
    def its_ok():
        """Test than object work"""
        return 'it\'s ok'
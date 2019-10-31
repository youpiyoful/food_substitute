"""This file contain the food object than map table food"""


class Food:
    """Representation of food entity"""

    def __init__(self, id_food, product_name,
                 generic_name, stores_tags, url, nutrigrade, id_category):
        """
        Initialize
        :param id_food:
        :param product_name:
        :param generic_name:
        :param stores_tags:
        :param url:
        :param nutrigrade:
        :param id_category:
        """
        self.id_food = id_food
        self.product_name = product_name
        self.generic_name = generic_name
        self.stores_tags = stores_tags
        self.url = url
        self.nutrigrade = nutrigrade
        self.id_category = id_category

    @staticmethod
    def its_ok():
        """Test than object work"""
        return 'it\'s ok'

    def get_food_best_than_me(self, list_of_food):
        """
        calcul the food than have the best nutriscore
        :param list_of_food:
        :return:
        """
        list_of_nutriscore_of_best_food = []

        for food_object in list_of_food:

            if food_object.nutrigrade <= self.nutrigrade:
                list_of_nutriscore_of_best_food.append(food_object.nutrigrade)

        print(list_of_nutriscore_of_best_food)
        if list_of_nutriscore_of_best_food:  # verify if best food exist
            nutriscore_of_best_food = min(list_of_nutriscore_of_best_food)
            print(nutriscore_of_best_food)

            for food_object in list_of_food:

                if nutriscore_of_best_food == food_object.nutrigrade:
                    return food_object

        else:
            return self

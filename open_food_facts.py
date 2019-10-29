"""This file processes data recovery and inserting into tables of our data base"""
import requests
import config
from config import list_of_keywords_interesting


class OpenFoodFact:
    def __init__(self, url_categories):
        self.url_categories = url_categories

    def retrieve_all_category_name_from_open_food_facts_api(self):
        """
        This function return a list of category's name of food from open food fact api
        :return list_of_new_category of food:
        """
        response = requests.get(self.url_categories)
        list_of_category = response.json().get('tags')
        list_of_new_category = []

        for category in list_of_category:
            new_category = {
                'category_name': category.get('name'),
                'url_category': category.get('url')
            }
            list_of_new_category.append(new_category)

        return list_of_new_category

    @staticmethod
    def retrieve_food_with_url_category(url_category, id_category):
        """
        :param url_category:
        :param id_category:

        :return:
        """
        response = requests.get(url_category + '.json')
        list_of_food = response.json().get('products')
        list_of_food_by_category = []

        for food in list_of_food:
            new_food = {
                'product_name': food.get('product_name'),
                'generic_name': food.get('generic_name'),
                'stores_tags': food.get('stores_tags'),
                'url': food.get('url'),
                'nutrition_grades': food.get('nutriscore_score'),
                'id_category': id_category
            }
            list_of_food_by_category.append(new_food)

        return list_of_food_by_category

    @staticmethod
    def filter_category_by_interest(list_of_new_category, list_of_keywords):  # idea : do a forbidden list !
        """
        :param list_of_new_category:
        :param list_of_keywords:
        :return list_of_interesting_category:
        """
        list_of_interesting_category = []

        for new_category in list_of_new_category:
            category_name = new_category.get('category_name')

            for keywords in list_of_keywords:

                if keywords in category_name:

                    if 'viande' not in category_name or 'lait' not in category_name:
                        list_of_interesting_category.append(new_category)
                        break

        return list_of_interesting_category


# response = OpenFoodFact()
# response.retrieve_all_category_name_from_open_food_facts_api()
# print(response.filter_category_by_interest(response, list_of_keywords_interesting))

"""This file processes data recovery and inserting into tables of our data base"""
import requests


class OpenFoodFact:
    def __init__(self, url_categories='https://fr.openfoodfacts.org/categories.json', number_min_food_by_category=10):
        self.url_categories = url_categories
        self.number_min_food_by_category = number_min_food_by_category

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

    def retrieve_food_with_url_category(self, url_category, id_category):
        """
        :param url_category:
        :param id_category:

        :return:
        """
        list_of_food_by_category = []
        num_page = 1
        number_of_product = 0

        # maximum_time = 10
        # tick = time.time()
        # todo verify number of product by page

        while len(list_of_food_by_category) <= self.number_min_food_by_category:
            response = requests.get(url_category + '/' + str(num_page) + '.json')
            list_of_food = response.json().get('products')
            print('list of food : ', list_of_food)
            # number_of_product += len(list_of_food)
            # print('number of product : ', number_of_product)
            num_page += 1
            print('number of page : ', num_page)
            # print(tick)
            # passed_time = time.time() - tick
            # print(passed_time)
            # if passed_time > maximum_time:
            #     break

            if len(list_of_food) == 0:
                break

            for food in list_of_food:

                if food.get('product_name') and food.get('generic_name') and food.get('url') and food.get(
                        'nutriscore_score') and id_category:
                    new_food = {
                        'product_name': food.get('product_name'),
                        'generic_name': food.get('generic_name'),
                        'stores_tags': food.get('stores_tags'),
                        'url': food.get('url'),
                        'nutrition_grades': food.get('nutriscore_score'),
                        'id_category': id_category
                    }
                    list_of_food_by_category.append(new_food)
            print(len(list_of_food_by_category))

            if len(list_of_food) < 20:
                break

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

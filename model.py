"""This file processes data recovery and inserting into tables of our data base"""
import requests

from config import list_of_keywords_interesting


def retrieve_all_category_name_from_open_food_facts_api():
    """
    This function return a list of category's name of food from open food fact api
    :return list of name of category food:
    """
    response = requests.get('https://fr.openfoodfacts.org/v0/categories.json')
    list_of_category = response.json().get('tags')
    list_of_category_names = []
    for category in list_of_category:
        name_category = category.get('name')
        list_of_category_names.append(name_category)

    return list_of_category_names


def filter_category_by_interest(list_of_category_names, list_of_keywords):  # idea : do a forbidden list !
    """
    :param list_of_category_names:
    :param list_of_keywords:
    :return list_of_interesting_category:
    """
    list_of_interesting_category = []
    for category_name in list_of_category_names:

        for keywords in list_of_keywords:

            if keywords in category_name:

                if 'viande' not in category_name or 'lait' not in category_name:
                    list_of_interesting_category.append(category_name)
                    break

    return list_of_interesting_category


response = retrieve_all_category_name_from_open_food_facts_api()
print(filter_category_by_interest(response, list_of_keywords_interesting))

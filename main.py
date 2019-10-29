import config
import manager
import open_food_facts

open_food_facts_object = open_food_facts.OpenFoodFact(
    url_category='https://fr.openfoodfacts.org/categories.json')  # instance of OpenFoodFact
manage_categories = manager.ManageCategories()  # instance of ManageCategories
manage_food = manager.ManageFood()  # instance of ManageFood


def retrieve_categories_from_open_food_facts_and_insert_in_our_db():
    """
    This is called only one time at start, for stock categories in our database
    :return:
    """
    all_categories_from_open_food_facts = open_food_facts_object.retrieve_all_category_name_from_open_food_facts_api()
    filtered_categories_by_interest = open_food_facts_object.filter_category_by_interest(
        all_categories_from_open_food_facts,
        config.list_of_keywords_interesting)  # use method of OpenFoodFact object than filter category by interest

    for filtered_category in filtered_categories_by_interest:
        print(filtered_category)
        manage_categories.insert_category_from_open_food_facts(filtered_category)


# retrieve_categories_from_open_food_facts_and_insert_in_our_db()


def retrieve_food_from_open_food_facts_and_insert_in_our_db():
    """
    This is called only one time at start, for stock foods in our database
    :return:
    """
    categories = manage_categories.get_category()

    for category_object in categories:
        list_of_food_by_category = open_food_facts_object.retrieve_food_with_url_category(category_object.url_category,
                                                                                          category_object.id_category)

        for food in list_of_food_by_category:
            manage_food.insert_food_from_open_food_facts(food)


# retrieve_food_from_open_food_facts_and_insert_in_our_db()
food = manage_food.get_food_by_name('Chips Allégées en Petit Sachet')
print(food.product_name)


def main():
    # food_by_name = manage_food.get_food_by_name(
    #     'test')  # use method of ManageFood than instantiate Food with data requested in db

    all_categories = manage_categories.get_category()  # use method
    print(all_categories[0])

    # for category in all_categories:  # run all category object in all_categories list
    #     print(category.id_category, category.category_name)  # display category attribute
    #
    # category_choice = int(input('Enter the num of your choice'))
    #
    # # print(food_by_name.product_name)  # display product name of food object
    # # print(food_by_name.__dict__)
    # print("""
    #             ########   #######   #######   ##########
    #            ##         ##   ##   ##   ##     ##    ##
    #           ######     ##   ##   ##   ##     ##    ##
    #          ##         ##   ##   ##   ##     ##    ##
    #         ##         #######   #######   ##########
    # """)
    # for key, value in food_by_name.__dict__.items():
    #     print(value)
    # print(all_categories.__doc__)


main()

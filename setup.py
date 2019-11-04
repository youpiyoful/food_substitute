"""File who create the database and populate him"""
import config
import open_food_facts
import manager

MANAGE_CATEGORIES = manager.ManageCategories()  # instance of ManageCategories
MANAGE_FOOD = manager.ManageFood()  # instance of ManageFood
# instance of OpenFoodFact
OPEN_FOOD_FACTS_OBJECT = open_food_facts.OpenFoodFact(config.url_categories,
                                                      config.number_min_food_by_category)


def retrieve_categories_from_open_food_facts_and_insert_in_our_db():
    """
    This is called only one time at start, for stock categories in our database
    :return:
    """
    all_categories_from_open_food_facts = \
        OPEN_FOOD_FACTS_OBJECT.retrieve_all_category_name_from_open_food_facts_api()
    # use method of OpenFoodFact object than filter category by interest
    filtered_categories_by_interest = OPEN_FOOD_FACTS_OBJECT.filter_category_by_interest(
        all_categories_from_open_food_facts,
        config.list_of_keywords_interesting)

    for filtered_category in filtered_categories_by_interest:
        print(filtered_category)
        MANAGE_CATEGORIES.insert_category_from_open_food_facts(filtered_category)


def retrieve_food_from_open_food_facts_and_insert_in_our_db():
    """
    This is called only one time at start, for stock foods in our database
    :return:
    """
    categories = MANAGE_CATEGORIES.get_category()

    for category_object in categories:
        list_of_food_by_category = OPEN_FOOD_FACTS_OBJECT.retrieve_food_with_url_category(
            category_object.url_category,
            category_object.id_category)

        for food in list_of_food_by_category:
            MANAGE_FOOD.insert_food_from_open_food_facts(food)


retrieve_food_from_open_food_facts_and_insert_in_our_db()
retrieve_categories_from_open_food_facts_and_insert_in_our_db()

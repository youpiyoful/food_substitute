import config
import manager
import open_food_facts

open_food_facts_object = open_food_facts.OpenFoodFact(config.url_categories,
                                                      config.number_min_food_by_category)  # instance of OpenFoodFact
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


def main():
    good_answer = False
    best_food = ""  # referenced before assignment to best_food variable

    while good_answer is False:
        start_choice = input(
            "For consult your substitution record push 1 | For launch the program of substitution push 2 : ")
        good_answer = True

    good_answer = False
    if start_choice == '2':
        all_categories = manage_categories.get_category_where_they_contain_15_food_min()  # use method

        for category in all_categories:  # run all category object in all_categories list
            print(category.id_category, category.category_name)  # display category attribute

        category_choice = int(input('Enter the num of your choice : '))

        list_of_food_by_id_category = manage_food.get_food_by_id_category(
            category_choice)  # use method of ManageFood than instantiate Food with data requested in db

        for food_by_id_category in list_of_food_by_id_category:
            print(food_by_id_category.id_food, food_by_id_category.product_name)

        food_choice = int(input('Enter the num of your choice : '))
        print(food_choice)

        for food_by_id_category in list_of_food_by_id_category:

            if food_choice == food_by_id_category.id_food:
                best_food = food_by_id_category.get_food_best_than_me(list_of_food_by_id_category)
                print('')
                print("              BEST FOOD                ")
                print('')
                print('id_food          : ', best_food.id_food)
                print('product_name     : ', best_food.product_name)
                print('generic name     : ', best_food.generic_name)
                print('stores_tags      : ', best_food.stores_tags)
                print('link to product  : ', best_food.url)
                print('nutriscore-score : ', best_food.nutrigrade)
                print('id_category      : ', best_food.id_category)

        while good_answer is False:
            response_to_record = input('Want you record substitute food ? y/n : ')

            if response_to_record is 'y':
                record_response = manage_food.record_substitute_food(food_choice, best_food.id_food)
                print(record_response)
                good_answer = True

            if response_to_record is 'n':
                print('don\'t record subsitute')
                good_answer = True

    else:
        # todo show record substitution
        pass

    print('                       END                   ')

    # print("""
    #             ########   #######   #######   ##########
    #            ##         ##   ##   ##   ##     ##    ##
    #           ######     ##   ##   ##   ##     ##    ##
    #          ##         ##   ##   ##   ##     ##    ##
    #         ##         #######   #######   ##########
    # """)


main()
# retrieve_food_from_open_food_facts_and_insert_in_our_db()
# retrieve_categories_from_open_food_facts_and_insert_in_our_db()

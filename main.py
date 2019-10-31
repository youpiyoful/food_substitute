"""Main file, where the program is executed"""
import manager

MANAGE_CATEGORIES = manager.ManageCategories()  # instance of ManageCategories
MANAGE_FOOD = manager.ManageFood()  # instance of ManageFood


def main():
    """
    main function than launch the program step by step
    :return:
    """
    good_answer = False
    best_food = ""  # referenced before assignment to best_food variable

    while good_answer is False:
        start_choice = input(
            'For consult your substitution record push 1 | For launch the program of substitution '
            'push 2 : ')
        good_answer = True

    good_answer = False
    if start_choice == '2':
        all_categories = MANAGE_CATEGORIES.get_category_where_they_contain_15_food_min()  # use
        # method

        for category in all_categories:  # run all category object in all_categories list
            print(category.id_category, category.category_name)  # display category attribute

        category_choice = int(input('Enter the num of your choice : '))

        list_of_food_by_id_category = MANAGE_FOOD.get_food_by_id_category(
            category_choice)  # use method of ManageFood than instantiate Food with data
        # requested in db

        for food_by_id_category in list_of_food_by_id_category:
            print(food_by_id_category.id_food, food_by_id_category.product_name)

        food_choice = int(input('Enter the num of your choice : '))
        print(food_choice)

        for food_by_id_category in list_of_food_by_id_category:

            if food_choice == food_by_id_category.id_food:
                best_food = food_by_id_category.get_food_best_than_me(list_of_food_by_id_category)
                print('')
                print('              BEST FOOD                ')
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

            if response_to_record == 'y':
                record_response = MANAGE_FOOD.record_substitute_food(food_choice, best_food.id_food)
                print(record_response)
                good_answer = True

            if response_to_record == 'n':
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

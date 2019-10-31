"""Main file, where the program is executed"""
import manager

MANAGE_CATEGORIES = manager.ManageCategories()  # instance of ManageCategories
MANAGE_FOOD = manager.ManageFood()  # instance of ManageFood


def main():
    """
    main function than launch the program step by step
    :return:
    """
    program_on = True

    while program_on is True:
        good_answer = False
        best_food = ""  # referenced before assignment to best_food variable
        start_choice = ""  # referenced before assignment to best_food variable
        leave_or_no = ""  # referenced before assignment to best_food variable
        category_choice = ""
        food_choice = ""
        list_of_id_category = []
        list_of_id_food = []

        while good_answer is False:  # start the program
            print('')
            start_choice = input(
                'For consult your substitution record push 1 | For launch the program of '
                'substitution '
                'push 2 : ')
            print('')

            if start_choice == '1' or start_choice == '2':
                good_answer = True

        good_answer = False
        if start_choice == '2':
            all_categories = MANAGE_CATEGORIES.get_category_where_they_contain_15_food_min()  # use
            # method

            for category in all_categories:  # run all category object in all_categories list
                print(category.id_category, category.category_name)  # display category attribute
                list_of_id_category.append(str(category.id_category))

            while category_choice not in list_of_id_category:
                print('')
                category_choice = input('Enter the num of your choice : ')
                print('')

            # use method of ManageFood than instantiate Food with data requested in db
            list_of_food_by_id_category = MANAGE_FOOD.get_food_by_id_category(
                category_choice)

            for food_by_id_category in list_of_food_by_id_category:
                print(food_by_id_category.id_food, food_by_id_category.product_name)
                list_of_id_food.append(str(food_by_id_category.id_food))

            while food_choice not in list_of_id_food:
                print('')
                # need to don t convert choice to int for handle bad string not only bad int
                food_choice = input('Enter the num of your choice : ')
                print('')

            for food_by_id_category in list_of_food_by_id_category:

                if food_choice == str(food_by_id_category.id_food):
                    best_food = food_by_id_category.get_food_best_than_me(
                        list_of_food_by_id_category)
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
                    print('')

            while good_answer is False:
                response_to_record = input('Want you record substitute food ? y/n : ')

                if response_to_record == 'y':
                    record_response = MANAGE_FOOD.record_substitute_food(food_choice,
                                                                         best_food.id_food)
                    print(record_response)
                    good_answer = True

                if response_to_record == 'n':
                    print('don\'t record subsitute')
                    good_answer = True

        else:

            substitutes_elements = MANAGE_FOOD.show_substitution()

            for substitute_el in substitutes_elements:
                print('---------------------------------------------------------------------------')
                print('category name            : ', substitute_el[0])
                print('product name substituted : ', substitute_el[1])
                print('substitute product name  : ', substitute_el[2])
                print('generic_name             : ', substitute_el[3])
                print('nutrition_grades         : ', substitute_el[4])
                print('stores_tags              : ', substitute_el[5])
                print('link                     : ', substitute_el[6])
                print('---------------------------------------------------------------------------')

        good_answer = False

        while good_answer is False:
            leave_or_no = input('Have you finished ? (y/n): ')

            if leave_or_no == 'y' or leave_or_no == 'n':
                good_answer = True

        if leave_or_no == 'y':
            program_on = False

        else:
            print('')
            print('                    COMEBACK TO MENU          ')
            print('')

    print('')
    print('                       END                   ')
    print('')

    # print("""
    #             ########   #######   #######   ##########
    #            ##         ##   ##   ##   ##     ##    ##
    #           ######     ##   ##   ##   ##     ##    ##
    #          ##         ##   ##   ##   ##     ##    ##
    #         ##         #######   #######   ##########
    # """)


main()

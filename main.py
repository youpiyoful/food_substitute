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

    while program_on is True:  # main loop, start the program
        good_answer = False  # variable of control
        best_food = ""  # referenced before assignment to best_food variable
        start_choice = ""  # referenced before assignment to best_food variable
        leave_or_no = ""  # referenced before assignment to best_food variable
        category_choice = ""  # referenced before assignment to best_food variable
        food_choice = ""  # referenced before assignment to best_food variable
        list_of_id_category = []
        list_of_id_food = []
        print("""
                        ########  ##    ##  ########  ########  ########  ########  ########  ##    ##  ########  ########
                       ##        ##    ##  ##    ##  ##           ##        ##        ##     ##    ##     ##     ##
                      ########  ##    ##  ##  ####  ########     ##        ##        ##     ##    ##     ##     ########
                           ##  ##    ##  ##    ##        ##     ##        ##        ##     ##    ##     ##     ##
                    ########  ########  ########   ########    ##     ########     ##     ########     ##     ########
        """)
        print("""
                                                    ########
        """)
        print("""
                    ########   #######   #######   ##########
                   ##         ##   ##   ##   ##     ##    ##
                  ######     ##   ##   ##   ##     ##    ##
                 ##         ##   ##   ##   ##     ##    ##
                ##         #######   #######   ##########
        """)
        # menu
        while good_answer is False:  # while good answer is false the loop continue
            print('')
            start_choice = input(
                'Pour consulter vos substituts enregistrés tapez 1 | Pour lancer le programme de '
                'substitution tapez 2 : ')  # offers 2 choices at user
            print('')

            if start_choice == '1' or start_choice == '2':  # if user do an offer choice,
                # good answer become true and the loop parent loop is done
                good_answer = True

        good_answer = False  # reset the variable of control

        if start_choice == '2':  # listen user's choice
            # recovers all categories containing more than 15 foods
            all_categories = MANAGE_CATEGORIES.get_category_where_they_contain_15_food_min()

            for category in all_categories:  # run all category object in all_categories list
                print(category.id_category, category.category_name)  # display category attribute
                # creates a category id list and converts them to a string
                list_of_id_category.append(str(category.id_category))

            while category_choice not in list_of_id_category:  # choice of the category
                print('')
                category_choice = input('Entrer le nombre correspondant à la catégorie de votre '
                                        'choix : ')
                print('')

            # use method of ManageFood than instantiate Food object with data requested in db
            list_of_food_by_id_category = MANAGE_FOOD.get_food_by_id_category(
                category_choice)

            #  display all the foods in the category chosen by the user
            for food_by_id_category in list_of_food_by_id_category:
                print(food_by_id_category.id_food, food_by_id_category.product_name)
                # save in a list the id foods and converts them into a chain
                list_of_id_food.append(str(food_by_id_category.id_food))

            # food choice that the user wants to substitute for a better product if there is one
            while food_choice not in list_of_id_food:
                print('')
                # don't convert the user's choice to an integer, even if it's necessary later,
                # to be able to manage the erroneous choices
                food_choice = input('Entrer le nombre correspondant à l\'aliment de votre choix : ')
                print('')

            # displays the substitute food of the user's chosen food only if it offers a better
            # nutrient
            for food_by_id_category in list_of_food_by_id_category:

                if food_choice == str(food_by_id_category.id_food):
                    best_food = food_by_id_category.get_food_best_than_me(
                        list_of_food_by_id_category)

                    if best_food:
                        print('')
                        print('             MEILLEUR ALIMENT             ')
                        print('')
                        print('Id aliment           : ', best_food.id_food)
                        print('Nom du produit       : ', best_food.product_name)
                        # print('Nom générique      : ', best_food.generic_name)
                        print('Magasins             : ', best_food.stores_tags)
                        print('Lien vers le produit : ', best_food.url)
                        print('Nutriscore           : ', best_food.nutrigrade)
                        print('Id categorie         : ', best_food.id_category)
                        print('')

                        #  4th step of the program, which proposes to the user to save the
                        #  substitution he
                        #  has just made
                        while good_answer is False:
                            response_to_record = input('Voulez enregistrer le substitut ? o/n : ')

                            if response_to_record == 'o':
                                record_response = MANAGE_FOOD.record_substitute_food(food_choice,
                                                                                     best_food.id_food)
                                print(record_response)
                                good_answer = True

                            if response_to_record == 'n':
                                print('Substitut non enregistré')
                                good_answer = True

                    else:
                        print('')
                        print('                 AUCUN MEILLEUR ALIMENT TROUVÉ        ')
                        print('')

        # part that displays the substitutions already made
        else:

            # uses the show_substitution method of the manage_food object
            substitutes_elements = MANAGE_FOOD.show_substitution()

            for substitute_el in substitutes_elements:  # formats the display
                print('---------------------------------------------------------------------------')
                print('Nom de la catégorie            : ', substitute_el[0])
                print('Nom du produit substitué       : ', substitute_el[1])
                print('Nom du subsitut                : ', substitute_el[2])
                # print('generic_name             : ', substitute_el[3])
                print('Nutriscore substitut           : ', substitute_el[4])
                print('Magasins                       : ', substitute_el[5])
                print('Lien vers le produit           : ', substitute_el[6])
                print('---------------------------------------------------------------------------')

        good_answer = False  # reset the control variable

        # last step that proposes to leave the program or return to the menu in the main loop
        while good_answer is False:
            leave_or_no = input('Avez-vous finis ? (o/n): ')  # listen user's choice

            if leave_or_no == 'o' or leave_or_no == 'n':  # control than answer is good
                good_answer = True

        if leave_or_no == 'o':  # verify if the user want leave the program
            # sets the program_on variable to false, which results in quitting the program
            # because the initial condition of the first loop is no longer satisfied
            program_on = False

        else:  # if answer is no the program comeback to the menu
            print('')
            print('                    RETOUR AU MENU             ')
            print('')

    print('')
    print('                       FIN                   ')
    print('')


main()

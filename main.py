import manager

manage_food = manager.ManageFood()  # instantiation of ManageFood

manage_categories = manager.ManageCategories()  # instantiation of ManageCategories

food_by_name = manage_food.get_food_by_name(
    'test')  # use method of ManageFood than instantiate Food with data requested in db

all_categories = manage_categories.get_category()  # use method

# for category in all_categories:  # run all category object in all_categories list
#     print(category.id_category, category.category_name)  # display category attribute
#
# print(food_by_name.product_name)  # display product name of food object
# print(food_by_name.__dict__)
print("""
            ########   #######   #######   ##########
           ##         ##   ##   ##   ##     ##    ##
          ######     ##   ##   ##   ##     ##    ##
         ##         ##   ##   ##   ##     ##    ##
        ##         #######   #######   ##########
""")
for key, value in food_by_name.__dict__.items():
    print(value)
# print(all_categories.__doc__)
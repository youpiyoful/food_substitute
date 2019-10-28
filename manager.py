import mysql.connector
import category
import food

from config import config

Error = mysql.connector.Error
myDb = mysql.connector.connect(user=config.get('user'), password=config.get('password'), host=config.get('host'),
                               port=config.get('port'), database=config.get('database'))


class ManageFood:

    @staticmethod
    def get_food_by_name(product_name):
        """Select food in table food by the product name"""
        try:
            cursor = myDb.cursor()
            query = f"""SELECT id_food, product_name, generic_name, stores_tags, url, nutrition_grades, id_category
                        FROM food WHERE product_name = "{product_name}";"""
            cursor.execute(query)
            results = cursor.fetchall()[0]
            myDb.commit()
            food_by_name = food.Food(results[0], results[1], results[2], results[3], results[4], results[5], results[6])
            print(results)
            return food_by_name

        except Error as e:
            message = f"select food encounter a mysql error : {e}"
            print(message)

    @staticmethod
    def insert_food_from_open_food_facts(food_object):
        """
        take a food object and insert it into the database
        :param food_object:
        :return:
        """
        try:
            cursor = myDb.cursor()
            query = f"""INSERT INTO food(product_name, generic_name, stores_tags, url, nutrition_grades, id_category)
                        values("{food_object.product_name}", "{food_object.generic_name}", "{food_object.stores_tags}",
                        "{food_object.url}", "{food_object.nutrition_grades}", "{food_object.id_category}");"""
            cursor.execute(query)
            myDb.commit()
            message = "insert_food_from_open_food_facts success"
            print(message)

        except Error as e:
            message = f"Error inserting food : {e}"
            print(message)


class ManageCategories:

    @staticmethod
    def get_category():
        """Select category in table category by the product name"""

        try:
            cursor = myDb.cursor()
            query = f"""SELECT id_category, name
                        FROM category;"""
            cursor.execute(query)
            results = cursor.fetchall()
            myDb.commit()
            print(results)
            array_of_categories = []

            for result in results:
                category_object = category.Category(result[0], result[1])
                array_of_categories.append(category_object)

            return array_of_categories

        except Error as e:
            message = f"select category encounter a mysql error : {e}"
            print(message)

    @staticmethod
    def insert_category_from_open_food_facts(category_object):
        """
        take a food object and insert it into the database
        :param category_object:
        :return:
        """
        try:
            cursor = myDb.cursor()
            query = f"""INSERT INTO category(name)
                        values("{category_object.category_name}")"""
            cursor.execute(query)
            myDb.commit()
            message = "insert_food_from_open_food_facts success"
            print(message)

        except Error as e:
            message = f"Error inserting food : {e}"
            print(message)
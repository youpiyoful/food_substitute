import mysql.connector

import category
import food
from config import config

Error = mysql.connector.Error
myDb = mysql.connector.connect(user=config.get('user'), password=config.get('password'), host=config.get('host'),
                               port=config.get('port'), database=config.get('database'))


class ManageFood:

    @staticmethod
    def get_food_by_id_category(id_category):
        """
        Select food in table food by the id of category
        :param id_category:
        :return:
        """
        try:
            cursor = myDb.cursor()
            query = f"""SELECT id_food, product_name, generic_name, stores_tags, url, nutrition_grades, id_category
                        FROM food WHERE id_category = {id_category};"""
            cursor.execute(query)
            results = cursor.fetchall()
            # print(results)
            myDb.commit()
            list_of_food_by_category = []
            for result in results:
                food_by_id_category = food.Food(id_food=result[0], product_name=result[1], generic_name=result[2],
                                                stores_tags=result[3], url=result[4], nutrigrade=result[5],
                                                id_category=result[6])
                list_of_food_by_category.append(food_by_id_category)
            # print(results)
            return list_of_food_by_category

        except Error as e:
            message = f"select food encounter a mysql error : {e}"
            print(message)

    @staticmethod
    def insert_food_from_open_food_facts(new_food):
        """
        take a new food and insert it into the database
        :param new_food:
        :return:
        """
        product_name = new_food.get('product_name')
        generic_name = new_food.get('generic_name')
        stores_tags = new_food.get('stores_tags')
        url = new_food.get('url')
        nutrition_grades = new_food.get('nutrition_grades')
        id_category = new_food.get('id_category')

        if product_name and generic_name and url and nutrition_grades and id_category:  # obvious data

            try:
                cursor = myDb.cursor()
                query = f"""INSERT INTO food(product_name, generic_name, stores_tags, url,
                            nutrition_grades, id_category)
                            values("{product_name}", "{generic_name}", "{stores_tags}",
                            "{url}", "{nutrition_grades}", "{id_category}");"""
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
            query = f"""SELECT id_category, name, url_category
                        FROM category;"""
            cursor.execute(query)
            results = cursor.fetchall()
            myDb.commit()
            # print(results)
            array_of_categories = []

            for result in results:
                result[2].replace("'", "''")
                category_object = category.Category(id_category=result[0], category_name=result[1],
                                                    url_category=result[2])
                array_of_categories.append(category_object)

            # print(array_of_categories)
            return array_of_categories

        except Error as e:
            message = f"select category encounter a mysql error : {e}"
            print(message)

    @staticmethod
    def get_category_where_they_contain_15_food_min():
        """Select category in table category by the product name"""

        try:
            cursor = myDb.cursor()
            query = f"""select c.id_category, c.name, c.url_category from category as c 
                        where c.id_category in (
                            select f.id_category from food as f group by id_category HAVING count(*) >= 15
                        )"""
            cursor.execute(query)
            results = cursor.fetchall()
            myDb.commit()
            # print(results)
            array_of_categories = []

            for result in results:
                result[2].replace("'", "''")
                category_object = category.Category(id_category=result[0], category_name=result[1],
                                                    url_category=result[2])
                array_of_categories.append(category_object)

            # print(array_of_categories)
            return array_of_categories

        except Error as e:
            message = f"select category encounter a mysql error : {e}"
            print(message)

    @staticmethod
    def insert_category_from_open_food_facts(new_category):
        """
        take a food object and insert it into the database
        :param new_category:
        :return:
        """
        category_name = new_category.get('category_name')
        url_category = new_category.get('url_category')

        if category_name and url_category:

            try:
                cursor = myDb.cursor()
                query = f"""INSERT INTO category(name, url_category)
                            values("{category_name}", "{url_category}")"""
                cursor.execute(query)
                myDb.commit()
                message = "insert_food_from_open_food_facts success"
                print(message)

            except Error as e:
                message = f"Error inserting food : {e}"
                print(message)

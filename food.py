import mysql.connector

from config import config

Error = mysql.connector.Error
myDb = mysql.connector.connect(user=config.get('user'), password=config.get('password'), host=config.get('host'),
                               port=config.get('port'), database=config.get('database'))


class Food:
    """Representation of food table"""

    def __init__(self):
        self.product_name = None
        self.generic_name = None
        self.stores_tags = None
        self.url = None
        self.nutrigrade = None
        self._id_category = None

    @staticmethod
    def select_food_by_name(self, product_name):
        """Select food in table food by the product name"""
        try:
            cursor = myDb.cursor()
            query = f"""SELECT id_food, product_name, generic_name, stores_tags, url, nutrition_grades, id_category
                        FROM food WHERE product_name = "{product_name}";"""
            cursor.execute(query)
            results = cursor.fetchall()
            myDb.commit()
            print(results)
            return results

        except Error as e:
            message = f"select food encounter a mysql error : {e}"
            print(message)
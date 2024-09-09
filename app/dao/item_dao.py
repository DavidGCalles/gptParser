# app/dao/item_dao.py

from app.services.db import get_db_connection

class ItemDAO:
    @staticmethod
    def get_all_items():
        connection = get_db_connection()
        if connection is None:
            return []

        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM items")
        items = cursor.fetchall()
        cursor.close()
        connection.close()
        return items

    @staticmethod
    def insert_item(item:dict):
        connection = get_db_connection()
        if connection is None:
            return False

        cursor = connection.cursor()
        query = """
        INSERT INTO items (receipt_id,user_id,description, quantity, unit_price, total_price)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            item['receipt_id'],
            item['user_id'],
            item['description'],
            item['quantity'],
            item['unit_price'],
            item['total_price']
        )
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return True
    
    @staticmethod
    def get_items_by_user_id(user_id:int):
        connection = get_db_connection()
        if connection is None:
            return []

        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM items WHERE user_id = {user_id}")
        items = cursor.fetchall()
        cursor.close()
        connection.close()
        return items

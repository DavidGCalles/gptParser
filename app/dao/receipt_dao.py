# app/dao/receipt_dao.py

from app.services.db import get_db_connection

class ReceiptDAO:
    @staticmethod
    def get_all_receipts():
        connection = get_db_connection()
        if connection is None:
            return []

        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM receipts")
        receipts = cursor.fetchall()
        cursor.close()
        connection.close()
        return receipts

    @staticmethod
    def insert_receipt(receipt:dict):
        connection = get_db_connection()
        if connection is None:
            return False

        cursor = connection.cursor()
        query = """
        INSERT INTO receipts (user_id,date, total, supermarket, payment_method, base64_image)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            receipt['user_id'],
            receipt['date'],
            receipt['total'],
            receipt['supermarket'],
            receipt['payment method'],
            receipt['base64_image']
        )
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return True
    
    @staticmethod
    def get_receipt_by_user_id(user_id:int):
        connection = get_db_connection()
        if connection is None:
            return []

        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM receipts WHERE user_id = {user_id}")
        receipts = cursor.fetchall()
        cursor.close()
        connection.close()
        return receipts

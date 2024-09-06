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
    def insert_receipt(receipt):
        connection = get_db_connection()
        if connection is None:
            return False

        cursor = connection.cursor()
        query = """
        INSERT INTO receipts (date, total, tax, supermarket, payment_method, base64_image)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            receipt['date'],
            receipt['total'],
            receipt['tax'],
            receipt['supermarket'],
            receipt['payment_method'],
            receipt['base64_image']
        )
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return True

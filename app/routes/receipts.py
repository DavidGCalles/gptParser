from flask import Blueprint, jsonify, request
from app.dao.receipt_dao import ReceiptDAO

# Define the blueprint for receipts
receipts_bp = Blueprint('receipts', __name__)

@receipts_bp.route('/', methods=['GET']) 
def get_receipts():
    receipts = ReceiptDAO.get_all_receipts()
    return jsonify(receipts), 200

@receipts_bp.route('/', methods=['POST']) 
def insert_receipt():
    receipt_data = request.get_json()
    success = ReceiptDAO.insert_receipt(receipt_data)
    if success:
        return jsonify({"message": "Receipt added successfully"}), 201
    else:
        return jsonify({"error": "Failed to add receipt"}), 500

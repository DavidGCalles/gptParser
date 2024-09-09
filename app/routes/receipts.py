from flask import Blueprint, jsonify, request
from app.dao.receipt_dao import ReceiptDAO
from app.dao.item_dao import ItemDAO
from app.utils.utils import build_option_headers

# Define the blueprint for receipts
receipts_bp = Blueprint('receipts', __name__)

@receipts_bp.route('/', methods=['GET']) 
def get_receipts():
    receipts = ReceiptDAO.get_all_receipts()
    return jsonify(receipts), 200

@receipts_bp.route('', methods=['POST', 'OPTIONS']) 
def insert_receipt():
    if request.method == "OPTIONS":
        response = build_option_headers()
        return response, 200
    receipt_data = request.get_json()
    success = ReceiptDAO.insert_receipt(receipt_data)
    if success is not None:
        for item in receipt_data["items"]:
            item["receipt_id"] = success
            item["user_id"] = receipt_data["user_id"]
            ItemDAO.insert_item(item)
        return jsonify({"message": "Receipt added successfully"}), 201
    else:
        return jsonify({"error": "Failed to add receipt"}), 500

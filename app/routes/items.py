from flask import Blueprint, jsonify, request
from app.dao.item_dao import ItemDAO
from app.utils.utils import build_option_headers

# Define the blueprint for receipts
items_bp = Blueprint('items', __name__)

@items_bp.route('/', methods=['GET']) 
def get_items():
    receipts = ItemDAO.get_all_items()
    return jsonify(receipts), 200

@items_bp.route('', methods=['POST', 'OPTIONS']) 
def insert_item():
    if request.method == "OPTIONS":
        response = build_option_headers()
        return response, 200
    item_data = request.get_json()
    success = ItemDAO.insert_item(item_data)
    if success:
        return jsonify({"message": "Receipt added successfully"}), 201
    else:
        return jsonify({"error": "Failed to add receipt"}), 500

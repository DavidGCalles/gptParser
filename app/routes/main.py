from flask import Blueprint, jsonify, request
from app.services.ticket_reader import TicketReader
from app.utils.utils import build_option_headers

main_bp = Blueprint('main', __name__)



@main_bp.route('/ping', methods=['GET'])
def ping():
    """
    Ping endpoint to test the server.
    ---
    responses:
      200:
        description: Server is running
        schema:
          type: object
          properties:
            message:
              type: string
              example: pong
    """
    return jsonify({"message": "pong"}),200

@main_bp.route('/receipt_parser', methods=['POST',"OPTIONS"])
def receipt_parser():
    if request.method == "OPTIONS":
        response = build_option_headers()
        return response, 200
    reader = TicketReader()
    json_data = request.get_json()
    request_data = {
        "base64_image": json_data.get("base64", None)}
    return jsonify(reader.parse_image(request_data)), 200

@main_bp.route('/basket_analyzer', methods=['POST', 'OPTIONS'])
def basket_analyzer():
    '''NO ES EL MOMENTO DE HACER ESTO'''
    if request.method == "OPTIONS":
        response = build_option_headers()
        return response, 200
    elif request.method == "POST":
        return {},500
        
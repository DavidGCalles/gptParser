import os

class Config:
    SECRET_KEY = 'your_secret_key'  # Replace with your actual secret key
    DB_HOST = 'localhost'
    DB_PORT = '3306'
    DB_NAME = 'receipt_analyzer'
    DB_USER = 'root'
    DB_PASSWORD = 'toor'
    SWAGGER = {
        'title': 'Flask API',
        'uiversion': 3
    }

    API_KEY = os.getenv("OPENAI_API_KEY")

    RECEIPT_MODEL_REQUIRED = {
        "supermarket": "string",
        "date": "string formated as yyyy-mm-dd",
        "items": "object array",
        "payment method": "cash or card",
        "total": "float"
    }

    ITEM_MODEL_REQUIRED = {
        "description": "string",
        "quantity": "number",
        "unit_price": "number",
        "total_price": "number"
    }

    PARSER_PROMPT = "You will receive an image from a supermarket receipt. I need you to return only a json "+\
        "object with the data fitting this model: "+\
        f"{RECEIPT_MODEL_REQUIRED} and items inside of it following this model: {ITEM_MODEL_REQUIRED}"
    
    ANALYZER_PROMPT = "You will receive a json object representing a supermarket receipt."+\
        "You have to split that bill in buying groups depending on the items."
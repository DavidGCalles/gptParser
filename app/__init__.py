from flask import Flask, request
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

def create_app():
    app = Flask(__name__, static_folder="static")
    CORS(app, expose_headers=['Content-Type'], supports_credentials=True, resources={r"/*": {"origins": "*"}})
    #CORS(app, expose_headers=['Content-Type'], supports_credentials=True)
    #CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
    #CORS(app, resources={r"/*": {"origins": "http://localhost:8081"}})

    # Register Blueprints
    from .routes.main import main_bp
    from .routes.receipts import receipts_bp
    app.register_blueprint(main_bp, url_prefix='/api')

    # Swagger UI setup
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'  # path to your API docs
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "Flask API", 'lang': "en"})
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    app.register_blueprint(receipts_bp, url_prefix='/api/receipts')

    return app

from flask import Flask, jsonify, json
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from sqlalchemy.orm import sessionmaker
from werkzeug.routing import BaseConverter
import decimal
from flask_login import LoginManager
try:
    from instance.config import ApplicationConfig
except Exception as e:
    from local_settings import ApplicationConfig
    
    
app = Flask(__name__)


app.config.from_object(ApplicationConfig)

session = sessionmaker()

check_enviroment = ApplicationConfig.CURRENT_SETTINGS
print(f"starting server with {check_enviroment} settings")


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)


app.url_map.converters['regex'] = RegexConverter
app.json_encoder = DecimalEncoder

digital_currency = ApplicationConfig.DIGITAL_CURRENCY
minconf = ApplicationConfig.MINCONF
minamount = ApplicationConfig.MIN_AMOUNT
maxamount = ApplicationConfig.MAX_AMOUNT
rpcusername = ApplicationConfig.RPC_USERNAME
rpcpassword = ApplicationConfig.RPC_PASSWORD
url = ApplicationConfig.URL


session.configure(bind=ApplicationConfig.SQLALCHEMY_DATABASE_URI_0)
db = SQLAlchemy(app)
server_session = Session(app)
ma = Marshmallow(app)

login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.anonymous_user = "Guest"



@app.errorhandler(500)
def internal_error500():
    return jsonify({"error": "Internal Error 500"}), 500


@app.errorhandler(502)
def internal_error502(error):
    return jsonify({"error": "Internal Error 502"}), 502


@app.errorhandler(404)
def internal_error404(error):
    return jsonify({"error": "Internal Error 400"}), 400


@app.errorhandler(401)
def internal_error404(error):
    return jsonify({"error": "Internal Error 401"}), 401


@app.errorhandler(400)
def internal_error400(error):
    return jsonify({"error": "Internal Error 400"}), 400


@app.errorhandler(413)
def to_large_file(error):
    return jsonify({"error": "File is too large.  Use a smaller image/file."}), 413


@app.errorhandler(403)
def internal_error403(error):
    return jsonify({"error": "Internal Error 403"}), 403


@app.errorhandler(405)
def internal_error(error):
    return jsonify({"error": "Internal Error 405"}), 405

# link locations
from .main import main as main_blueprint
app.register_blueprint(main_blueprint, url_prefix='/main')


from .info import info as info_blueprint
app.register_blueprint(info_blueprint, url_prefix='/info')

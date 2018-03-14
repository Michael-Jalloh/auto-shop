from flask import Flask, render_template
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import logging
from models import RevokedToken
import car, user


application = Flask(__name__,
                    static_folder='./dist/static',
                    template_folder='./dist')
application.config.from_object('config')
jwt = JWTManager(application)
api = Api(application)
CORS(application, resources={r"/api/*":{"origin":"*"}})

@jwt.token_in_blacklist_loader
def check_token(decrypted_token):
    jti = decrypted_token['jti']
    return RevokedToken.is_jti_blacklisted(jti)


@application.route('/')
def index():
    return render_template('index.html')

# Set up the logger
logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

# Formatter for logger
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh = logging.FileHandler("Track.log")
fh.setFormatter(formatter)

logger.addHandler(fh)
logger.info('=========================START=========================')

api.add_resource(user.Signup, '/api/v1/signup'"")
api.add_resource(car.AddCar, '/api/v1/add-car')
api.add_resource(car.GetCars, '/api/v1/get-cars')
api.add_resource(car.ViewCar, '/api/v1/view-car')


api.add_resource(car.TestCar, '/api/v1/test-car')

if __name__ =='__main__':
    application.run(host='0.0.0.0')

from flask import Flask, render_template, send_from_directory, request
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from models import Car
import logging
from models import RevokedToken
import car, user, profile

UPLOAD_FOLDER = "static/img"
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

@application.route('/get-photo/<path:id>')
def send_photo(id):
    c = Car.get(id=int(id))
    return send_from_directory(UPLOAD_FOLDER,c.pics)

@application.route('/post/images', methods=["POST"])
def images():
        img = request.form.get('image')
        name = request.form.get('name')
        print name
        i = open(name)
        i.write(img)
        i.save()
        return ''

# Set up the logger
logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

# Formatter for logger
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh = logging.FileHandler("Track.log")
fh.setFormatter(formatter)

logger.addHandler(fh)
logger.info('=========================START=========================')


api.add_resource(user.Signup, '/api/v1/sign-up')
api.add_resource(user.Login, '/api/v1/login')
api.add_resource(user.TokenRefresh,'/api/v1/token-refresh')
api.add_resource(user.LogoutAccessToken, '/api/v1/logout-access')
api.add_resource(user.LogoutRefreshToken, '/api/v1/logout-refresh')


api.add_resource(car.AddCar, '/api/v1/add-car')
api.add_resource(car.EditCar, '/api/v1/edit-car')
api.add_resource(car.GetCars, '/api/v1/get-cars')
api.add_resource(car.GetCar, '/api/v1/get-car/<path:car_id>')
api.add_resource(car.GetMyCars, '/api/v1/my-cars/')
api.add_resource(car.PhotoUpload,'/api/v1/upload-photo')
api.add_resource(car.UserCars, '/api/v1/user-cars/<path:user>')
api.add_resource(car.DeleteCar, '/api/v1/delete-car/<path:id>')
api.add_resource(car.GetImagebyId, '/api/v1/get-image-by-id/<path:id>')
api.add_resource(car.CarType, '/api/v1/get-cars/<path:car_type>')
api.add_resource(car.FeaturedCars, '/api/v1/featured-cars')

api.add_resource(profile.ProfileUpload, '/api/v1/upload-profile')
api.add_resource(profile.GetProfilePic,'/api/v1/get-profile-pic/<path:user_id>')
api.add_resource(profile.EditProfile,'/api/v1/edit-profile')
api.add_resource(profile.GetProfile,'/api/v1/get-profile/<path:user_id>')


api.add_resource(car.GetImage, '/api/v1/get-image/<path:filename>')



if __name__ =='__main__':
    application.run(host='0.0.0.0', port=5000)

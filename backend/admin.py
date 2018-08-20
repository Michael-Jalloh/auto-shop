from flask_restful import Resource, reqparse
from flask import send_from_directory
import werkzeug
import os
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity
import logging, datetime
from models import User, Car, Info

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('price')
parser.add_argument('description')
parser.add_argument('pics')
parser.add_argument('model')
parser.add_argument('brand')
parser.add_argument('body_type')
parser.add_argument('year')
parser.add_argument('search')
parser.add_argument('user')
parser.add_argument('transmission')
parser.add_argument('engine')
parser.add_argument('mileage')
parser.add_argument('fuel')
parser.add_argument('drive_train')
parser.add_argument('published')
parser.add_argument('car_id')
parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
parser.add_argument('pic_name')
parser.add_argument('car_id')
parser.add_argument('car_type')
parser.add_argument('type')
parser.add_argument('featured')
parser.add_argument('flagged')
parser.add_argument('ads-name')
parser.add_argument('facebook')
parser.add_argument('twitter')
parser.add_argument('instagram')

UPLOAD_FOLDER = "static/img"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allow_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_date():
    date = str(datetime.datetime.now()).replace(' ', '-')
    date = date.replace(':','-')
    return date.replace('.','-').encode('hex')

def remove_file(filename):
    filename = os.path.join(UPLOAD_FOLDER,filename)
    if os.path.isfile:
        os.remove(filename)


class AdminGetCars(Resource):
    decorators = [jwt_required]
    def get(self):
        user = User.get(id = int(get_jwt_identity()))
        if user.account_type != 'admin':
            return {}, 401
        cars = [car.dictionary() for car in Car.select()]
        return {
            'data':cars,
            'message':'',
            'status':'success'
            }


class AdminDeleteCar(Resource):

    decorators = [jwt_required]

    def delete(self, id):
        try:
            user = User.get(id = int(get_jwt_identity()))
            if user.account_type != 'admin':
                return {}, 401

            if (user == 'admin'):
                car = Car.get(id=int(id))
                car.delete_instance()

                return {
                    'data': '',
                    'messsage': 'Car deleted',
                    'status': 'success'
                    }
            return {
                'data': '',
                'message': 'Forbidden',
                'status': 'error'
                }
        except Exception as e:
            print str(e)

            return {
                'data': '',
                'message': "Car couldn't be deleted",
                'status': 'success'
                }

class FlaggedCars(Resource):

  decorators = []

  def get(self):
    logger = logging.getLogger('app.get-car-')

    cars = [car.dictionary() for car in Car.select().where(Car.flagged == True)]

    return {
        'data': cars,
        'message':'',
        'status':'success'
        }

class AdminFeatured(Resource):
  decorators = [jwt_required]

  def post(self):
    logger = logging.getLogger('app.post-admin-featured')
    data = parser.parse_args()

    try:
        user = User.get(id = int(get_jwt_identity()))
        if user.account_type != 'admin':
            return {}, 401
        car = Car.get(id=int(data['car_id']))
        car.featured = False
        if data['featured'] == 'True':
            car.featured =  True

        car.save()
        if car.featured:
            return {
                    'data':'Featured',
                    'message':'Car {} has been featured'.format(car.name),
                    'status': 'success'
                    }
        return {
            'data': 'Featured',
            'message':'Car {} has been removed from the featured cars'.format(car.name),
            'status':'success'
            }

    except Exception as e:
        print str(e)
        logger.error(e)
        return {
                'data':'',
                'message':'An error occur',
                'status': 'error'
                }

class AdminPublished(Resource):
  decorators = [jwt_required]

  def post(self):
    logger = logging.getLogger('app.post-admin-published')
    data = parser.parse_args()
    try:
        user = User.get(id = int(get_jwt_identity()))
        if user.account_type != 'admin':
            return {}, 401

        car = Car.get(id=int(data['car_id']))
        car.published = False
        if data['published'] == 'True':
            car.published =  True

        car.save()
        if car.published:
            return {
                    'data':'',
                    'message':'Car {} has been published'.format(car.name),
                    'status': 'success'
                    }
        return {
            'data': '',
            'message':'Car {} has been removed from the published cars'.format(car.name),
            'status':'success'
            }

    except Exception as e:
        print str(e)
        logger.error(e)
        return {
                'data': '',
                'message': 'An error occur',
                'status': 'error'
                }

class AdminUsers(Resource):
    decorators = [jwt_required]

    def get(self):
        users = [user.dictionary() for user in User.select()]
        return {
            'data':users,
            'message': '',
            'status':'success'
            }

class AdminFlagCar(Resource):
    decorators = [jwt_required]

    def post(self):
        user = User.get(id = int(get_jwt_identity()))
        if user.account_type != 'admin':
            return {}, 401

        data = parser.parse_args()
        logger = logging.getLogger('app.admin-flagger')
        car = Car.get(id=int(data['car_id']))

        car.flagged = False
        if data['flagged'] == 'True':
            car.flagged = True

        car.save()
        return {
            'data': '',
            'message': 'Updated',
            'status': ''
            }

class DeleteUser(Resource):
    decorators = [jwt_required]

    def delete(self, id):
        user = User.get(id = int(get_jwt_identity()))
        if user.account_type != 'admin':
            return {}, 401

        del_user = User.get(id=int(id))
        del_user.delete_instance()

        return {
            'data':'',
            'message':'User deleted',
            'status':''
            }

class AdsImages(Resource):
    decorators = [jwt_required]

    def get(self):
        user = User.get(id = int(get_jwt_identity()))
        if user.account_type != 'admin':
            return {}, 401
        ads_left = Info.get(name="ads-left")
        return {
            'status':'OK',
            'message':'',
            'data':[ads_left.dictionary()]
        }

    def post(self):
        user = User.get(id = int(get_jwt_identity()))
        if user.account_type != 'admin':
            return {}, 401

        data = parser.parse_args()
        print data
        info = Info.get(name=data['ads-name'])
        if data['file'] == '':
            return {
                    'data':'',
                    'message':'No photo found',
                    'status':'Error'
                    }
        photo = data['file']
        if photo:
            if info.value:
                remove_file(info.value)
                print 'Updating'
            else:
                print 'Creating'
            info.value = get_date()+'.png'
            photo.save(os.path.join(UPLOAD_FOLDER, info.value))
            info.save()
        return {
            'data': info.dictionary(),
            'status':'',
            'message':''
            }

class GetAds(Resource):
    def get(self):
        ad = Info.get(name="ads-left")
        return {
            'data':ad.dictionary(),
            'status':'OK',
            'message':''
        }

class SocialMedia(Resource):
    decorators = [jwt_required]

    def get(self):
        user = User.get(id = int(get_jwt_identity()))
        if user.account_type != 'admin':
            return {}, 401

        links = ['facebook','twitter','instagram']
        social_media = {}
        for link in Info.select():
                if link.name in links:
                    social_media[link.name] = link.value
                    print link.name, link.value
        return {
            'data':social_media,
            'message':'',
            'status':'OK'
        }

    def post(self):
        user = User.get(id = int(get_jwt_identity()))
        if user.account_type != 'admin':
            return {}, 401

        data = parser.parse_args()
        facebook = Info.get(name="facebook")
        twitter = Info.get(name="twitter")
        instagram = Info.get(name="instagram")
        print data

        if data['facebook']:
            facebook.value = data['facebook']
            facebook.save()
        if data['twitter']:
            twitter.value = data['twitter']
            twitter.save()
        if data['instagram']:
            instagram.value = data['instagram']
            instagram.save()

        return {
            'data':'',
            'message':'',
            'status':'OK'
            }

class GetSocials(Resource):
    def get(self):
        links = ['facebook','twitter','instagram']
        social_media = {}
        for link in Info.select():
                if link.name in links:
                    social_media[link.name] = link.value
        return {
            'data':social_media,
            'message':'',
            'status':'OK'
        }

from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
import logging
from models import User, Car

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

class AddCar(Resource):
    decorators = []

    def post(self):
        data = parser.parse_args()
        logger = logging.getLogger('app.add-car-get')
        car = Car()
        car.name = data['name']
        car.price = data['price']
        car.description = data['description']
        car.brand = data['brand']
        car.model = data['model']
        car.year = data['year']
        car.transmission = data['transmission']
        car.engine = data['engine']
        car.mileage = data['mileage']
        car.fuel = data['fuel']
        car.drive_train = data['drive_train']
        try:
            car.owner = User.get(id=int(data['user']))
            car.save()
            return {
                'data':Car.car_to_dict(car),
                'message':'Post saved',
                'status':'success'
                }
        except Exception as e:
            logger.error(str(e))
            return {
                'data':'',
                'message':'And error occur please check your fields',
                'status':'error'
                }

class GetCars(Resource):
    decorators=[]

    def get(self):
        cars = Car.select()
        query = []
        for car in cars:
            query.append(Car.car_to_dict(car))

        return {
                'data':query,
                'message':'',
                'status':'success'
                }

class ViewCar(Resource):
    decorators = []

    def post(self):
        data = parser.parse_args()
        logger = logging.getLogger('app.view-car-post')
        car_id = data['car_id']
        try:
            car = Car.car_to_dict(Car.get(id=int(car_id)))
            return {
                'message':'',
                'data': car,
                'status':'succes'
                }
        except Exception as e:
            logger.error(str(e))
            return {
                    'message':'An error occur',
                    'data':'',
                    'status':'error'
                    }
                    

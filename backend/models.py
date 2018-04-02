from peewee import *
from playhouse.sqlite_ext import *
from playhouse.postgres_ext import *
from playhouse.flask_utils import get_object_or_404
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import json


db = SqliteExtDatabase('auto_shop.db')
#db = PostgresqlExtDatabase('test',user='michael', password='millicent', register_hstore=False)
class BaseModel(Model):
    class Meta:
        database = db

class RevokedToken(BaseModel):
    jti = CharField()


    @classmethod
    def is_jti_blacklisted(cls,jti):
        try:
            jti = RevokedToken.get(jti=jti)
            return True
        except:
            return False

class User(BaseModel):
    username = CharField(unique=True)
    account_type = CharField(default="individual")
    logo = CharField(default='')
    password_hash = CharField()
    email = CharField(unique=True)
    contact = CharField(default="")
    joined = DateTimeField(default=datetime.datetime.now())

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash, password)

class Car(BaseModel):
    name = CharField()
    price = CharField(default="")
    description = TextField(default="")
    pics = CharField(default="")
    brand = CharField(default="")
    model = CharField(default="")
    body_type = CharField(default="")
    year = DateField(formats=['%d-%m-%Y'], default='01-Jan-2000')
    transmission = CharField(default="")
    engine = CharField(default="")
    mileage = IntegerField()
    car_type = CharField(default="")
    fuel = CharField(default="")
    drive_train = CharField(default="")
    owner = ForeignKeyField(User, related_name="cars")
    created = DateTimeField(default=datetime.datetime.now())
    published = BooleanField(default=False)

    @staticmethod
    def car_to_dict(car):
        return {
            'name': car.name,
            'car_id': car.id,
            'price': car.price,
            'description': car.description,
            'brand': car.brand,
            'model': car.model.capitalize(),
            'year': car.year.split('-')[0],
            'transmission': car.transmission.capitalize(),
            'engine': car.engine,
            'mileage': car.mileage,
            'fuel': car.fuel.capitalize(),
            'drive_train': car.drive_train,
            'owner': {
                        'username':car.owner.username,
                        'id':car.owner.id
                      },
            'created': str(car.created),
            'pic': car.pics
            }

class Brand(BaseModel):
    value = CharField(unique=True)

class BodyType(BaseModel):
    value = CharField(unique=True)

class Category(BaseModel):
    value = CharField(unique=True)


def create_tables():
    db.create_tables([User, Car, Brand, BodyType, Category],safe=True)

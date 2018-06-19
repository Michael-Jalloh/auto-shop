from peewee import *
from playhouse.sqlite_ext import *
from playhouse.postgres_ext import *
from playhouse.flask_utils import get_object_or_404
import datetime
from hashlib import md5
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
    location = CharField(default="")
    joined = DateTimeField(default=datetime.datetime.now())
    avatar = CharField(default="avatar.png")
    bio = TextField(default="")
    active = BooleanField(default=False)
    email_confirm = BooleanField(default=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash, password)

    def get_cars(self):
        cars = [car.dictionary() for car in Car.select().join(User).where(User.id == self.id)]
        return cars

    def dictionary(self):
        return {
            'username': self.username,
            'account_type':self.account_type,
            'id': self.id,
            'email':self.email,
            'contact':self.contact,
            'location': self.location,
            'avatar':  self.avatar,
            'bio': self.bio
        }

    def avt(self,size=28):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)


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
    featured = BooleanField(default=False)


    def dictionary(self):
        return {
            'name': self.name,
            'car_id': self.id,
            'price': self.price,
            'description': self.description,
            'brand': self.brand,
            'model': self.model.capitalize(),
            'year': str(self.year).split('-')[0],
            'transmission': self.transmission.capitalize(),
            'engine': self.engine,
            'mileage': self.mileage,
            'fuel': self.fuel.capitalize(),
            'drive_train': self.drive_train,
            'owner': self.owner.dictionary(),
            'created': str(self.created),
            'pic': self.pics,
            'type': self.car_type
            }

class Brand(BaseModel):
    value = CharField(unique=True)

class BodyType(BaseModel):
    value = CharField(unique=True)

class Category(BaseModel):
    value = CharField(unique=True)


class Blog(BaseModel):
    timestamp = DateTimeField(default=datetime.datetime.now())
    published = BooleanField(default=False)
    content = TextField(default="")


    def publish(self):
        self.published = True
        self.timestamp = datetime.datetime.now()
        self.save()



def create_tables():
    db.create_tables([User, Car, Brand, BodyType, Category, Blog],safe=True)

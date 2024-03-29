from peewee import *
from playhouse.sqlite_ext import *
from playhouse.postgres_ext import *
from playhouse.flask_utils import get_object_or_404
import datetime
from hashlib import md5
from werkzeug.security import generate_password_hash, check_password_hash
import json
import urlparse

pragmas = [
        ('journal_mode','wal'),
        ('cache_size',-1000 * 32)]
db = SqliteExtDatabase('auto_shop.db', pragmas=pragmas)

#db = PostgresqlExtDatabase('test',user='michael', password='millicent', register_hstore=False)

class JsonField(TextField):
    """Store JSON data in a TextField"""
    def python_value(self, value):
        if value is not None:
            return json.loads(value)

    def db_value(self, value):
        if value is not None:
            return json.dumps(value)

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
    pictures = TextField(default="")
    brand = CharField(default="")
    model = CharField(default="")
    body_type = CharField(default="")
    year = DateField(formats=['%d-%m-%Y'], default='01-Jan-2000')
    transmission = CharField(default="")
    engine = CharField(default="")
    mileage = CharField()
    car_type = CharField(default="")
    fuel = CharField(default="")
    drive_train = CharField(default="")
    owner = ForeignKeyField(User, related_name="cars")
    created = DateTimeField(default=datetime.datetime.now())
    published = BooleanField(default=False)
    featured = BooleanField(default=False)
    flagged = BooleanField(default=False)
    flagger = CharField(default="")
    flag_reason = TextField(default="")

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
            'type': self.car_type,
            'featured': self.featured,
            'flagged': self.flagged,
            'flagger': self.flagger,
            'flag_reason': self.flag_reason,
            'published': self.published,
            'pictures': self.pictures
            }

    def add_search(self):
        FTSCar.create(
        docid = self.id,
        content = '\n'.join((self.name, str(self.price), self.description, self.brand, self.model, str(self.year), self.transmission, self.engine, str(self.mileage), self.fuel, self.drive_train, str(self.created), self.car_type))
        )

class Brand(BaseModel):
    value = CharField(unique=True)

class BodyType(BaseModel):
    value = CharField(unique=True)

class Category(BaseModel):
    value = CharField(unique=True)

class Post(BaseModel):
    title = CharField()
    content = TextField(default="")
    created = DateTimeField(default=datetime.datetime.now())
    published = BooleanField(default=False)
    timestamp = DateTimeField(default=datetime.datetime.now())
    pic = CharField(default='')
    pics = CharField(default='')
    post_type = CharField(default="post")

    def publish(self):
        self.published = True
        self.timestamp = datetime.datetime.now()
        self.save()


    @classmethod
    def get_published_post(cls):
        posts = [post.dictionary() for post in Post.select().where((Post.published==True) & (Post.post_type =="post"))]
        return posts

    @classmethod
    def get_published_pages(cls):
        pages = [post.dictionary() for post in Post.select().where((Post.published==True) & (Post.post_type =="page"))]
        return pages

    @classmethod
    def get_all_post(cls):
        posts = [post.dictionary() for post in Post.select()]
        return posts

    @classmethod
    def get_drafts(cls):
        posts = [post.dictionary() for post in Post.select().where(Post.published==False)]
        return posts

    def dictionary(self):

        return {
            'title': self.title,
            'id': self.id,
            'publish': self.published,
            'timestamp': str(self.timestamp),
            'content': self.content,
            'pic': self.pic
            }

    def add_search(self):
        FTSBlog.create(
            docid=self.id,
            content='\n'.join((self.title, self.content))
        )

class FeedBack(BaseModel):
    name = CharField(default="")
    last_name = CharField(default="")
    email = CharField(default="")
    tel = CharField(default="")
    msg = TextField(default="")

    def dictionary(self):
        return {
            'name': self.name,
            'last_name': self.last_name,
            'email': self.email,
            'tel': self.tel,
            'msg': self.msg
        }

class Info(BaseModel):
    name = CharField(unique=True)
    value = CharField(default="")

    def dictionary(self):
        return {
            'name':self.name,
            'value':self.value}

class Tracker(BaseModel):
    domain = CharField()
    url = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now, index=True)
    post_id = IntegerField()
    title = TextField(default="")
    page_type = CharField(default="")
    ip = CharField(default="")
    referrer = TextField(default="")
    headers = JsonField()
    params = JsonField()

    def dictionary(self):
        return {
            "domain":self.domain,
            "url":self.url,
            "timestamp":str(self.timestamp),
            "post_id":self.post_id,
            "title":self.title,
            "page_type":self.page_type,
            "ip":self.ip,
            "referrer": self.referrer,
            "params":self.params
        }

    @classmethod
    def create_from_request(cls, **data):
        request = data.get("request")
        print "[*] Model Request:", request.url
        parsed = urlparse.urlparse(request.url)
        params = dict(urlparse.parse_qsl(parsed.query))
        print params
        print "[*] parsed", parsed
        print "[*] Name:", data['name']

        return Tracker.create(
            domain=parsed.netloc,
            url=parsed.path,
            title=data.get("name",''),
            page_type=data.get('type',''),
            post_id = int(data.get("tracker_id", 0)),
            ip = request.headers.get('X-Forwarded-For', request.remote_addr),
            referrer=request.args.get('ref',""),
            headers=dict(request.headers),
            params=params)

class Log(BaseModel):
    logger = CharField()
    level = CharField()
    trace = TextField(default="")
    msg = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return "Logger: {}, Level: {}, Trace: {}, Msg: {}, Timestamp: {}".format(self.logger, self.level, self.trace, self.msg, str(self.timestamp))

    def dictionary(self):
        return {
            "logger": self.logger,
            "level": self.level,
            "trace": self.trace,
            "msg": self.msg,
            "timestamp": str(self.timestamp).split('.')[0]
        }


class FTSBlog(FTSModel):
    content = TextField()

    class Meta:
        database =db

class FTSCar(FTSModel):
    content = TextField()

    class Meta:
        database = db




def create_tables():
    db.create_tables([User, Car, Brand, BodyType, Category, Blog, FeedBack, Info, FTSBlog, FTSCar, Tracker, Log],safe=True)

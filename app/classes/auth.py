# coding=utf-8
from app import db
from datetime import datetime


class Auth_UserFees(db.Model):
    __tablename__ = 'userfees'
    __bind_key__ = 'clearnet'
    __table_args__ = {"schema": "public", 'extend_existing': True}

    id = db.Column(db.Integer, autoincrement=True,
                   primary_key=True, unique=True)
    user_id = db.Column(db.INTEGER)
    buyerfee = db.Column(db.DECIMAL(6, 4))
    buyerfee_time = db.Column(db.TIMESTAMP())
    vendorfee = db.Column(db.DECIMAL(6, 4))
    vendorfee_time = db.Column(db.TIMESTAMP())


class Auth_AccountSeedWords(db.Model):
    __tablename__ = 'AccountSeedWords'
    __bind_key__ = 'clearnet'
    __table_args__ = {"schema": "public", 'extend_existing': True}

    id = db.Column(db.Integer, autoincrement=True,
                   primary_key=True, unique=True)
    user_id = db.Column(db.INTEGER)
    word00 = db.Column(db.VARCHAR(30))
    word01 = db.Column(db.VARCHAR(30))
    word02 = db.Column(db.VARCHAR(30))
    word03 = db.Column(db.VARCHAR(30))
    word04 = db.Column(db.VARCHAR(30))
    word05 = db.Column(db.VARCHAR(30))
    wordstring = db.Column(db.TEXT)


class Auth_User(db.Model):
    __tablename__ = 'users'
    __bind_key__ = 'clearnet'
    __table_args__ = {"schema": "public", 'extend_existing': True}

    id = db.Column(db.Integer, autoincrement=True,
                   primary_key=True, unique=True)
    username = db.Column(db.TEXT)
    password_hash = db.Column(db.TEXT)
    member_since = db.Column(db.TIMESTAMP(), default=datetime.utcnow())
    email = db.Column(db.TEXT)
    wallet_pin = db.Column(db.TEXT)
    profileimage = db.Column(db.TEXT)
    stringuserdir = db.Column(db.TEXT)
    bio = db.Column(db.TEXT)
    country = db.Column(db.TEXT)
    currency = db.Column(db.INTEGER)
    vendor_account = db.Column(db.INTEGER)
    selling_from = db.Column(db.TEXT)
    last_seen = db.Column(db.TIMESTAMP(), default=datetime.utcnow())
    admin = db.Column(db.INTEGER)
    admin_role = db.Column(db.INTEGER)
    dispute = db.Column(db.INTEGER)
    fails = db.Column(db.INTEGER)
    locked = db.Column(db.INTEGER)
    vacation = db.Column(db.INTEGER)
    shopping_timer = db.Column(db.TIMESTAMP())
    lasttraded_timer = db.Column(db.TIMESTAMP())
    shard = db.Column(db.INTEGER)
    usernode = db.Column(db.INTEGER)
    affiliate_account = db.Column(db.INTEGER)
    confirmed = db.Column(db.INTEGER)
    passwordpinallowed = db.Column(db.INTEGER)




db.configure_mappers()
db.create_all()
db.session.commit()

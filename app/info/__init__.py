# coding=utf-8
from flask import Blueprint


info = Blueprint('info', __name__)


from . import views
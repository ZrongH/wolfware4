# -*- coding: utf-8 -*-
from mongoengine.connection import connect
from mongoengine.document import Document
from mongoengine.fields import IntField, StringField

__author__ = 'yeshiming@gmail.com'

connect('test')

class Code(Document):
    access_token = StringField()
    expires_in = IntField()
    code = StringField()

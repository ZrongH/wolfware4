# -*- coding: utf-8 -*-
from mongoengine.connection import connect
from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import IntField, StringField, ReferenceField

__author__ = 'yeshiming@gmail.com'

connect('test')

class Code(Document):
    access_token = StringField()
    expires_in = IntField()
    code = StringField()

class Users(Document):
    name = StringField()
    student_id = IntField()

class Contact(Document):
    user = ReferenceField(User)
    address = StringField()
    tel = StringField()
# -*- coding: utf-8 -*-
from mongoengine.connection import connect
from mongoengine.document import Document
from mongoengine.fields import IntField, StringField, ReferenceField

__author__ = 'yeshiming@gmail.com'

connect('test')

class Code(Document):
    access_token = StringField()
    expires_in = IntField()
    code = StringField()

class User(Document):
    name = StringField()
    student_id = IntField()
    address = StringField()
    tel = StringField()
    qq = StringField()
    email = StringField()

def get_unicode(str):
    if isinstance(str, unicode):
        return str
    for c in ('utf8', 'gbk'):
        return str.decode(c)
    return str

def load_data():
    for line in open('init_data/students', 'r'):
        student_id, name = line.split(",")
        User.objects.insert(User(name = get_unicode(name), student_id=get_unicode(student_id)))

if not User.objects().count():
    load_data()




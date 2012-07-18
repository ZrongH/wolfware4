# -*- coding: utf-8 -*-
import datetime
from mongoengine.document import Document
from mongoengine.fields import StringField, DateTimeField

__author__ = 'yeshiming@gmail.com'

class Message(Document):
    content = StringField()
    publish_date = DateTimeField(default=datetime.datetime.now)
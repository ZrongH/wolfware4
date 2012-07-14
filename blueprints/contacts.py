# -*- coding: utf-8 -*-

"""
Ajax requests of account operation.
"""

from flask.blueprints import Blueprint
from flask.globals import current_app, request
from flask.helpers import jsonify
from flask.templating import render_template
from models import User

__author__ = 'yeshiming@gmail.com'

app = current_app
contacts_bp = Blueprint('contacts', __name__, template_folder='templates')

@contacts_bp.route('/', methods = ['GET'])
def index():
    return render_template('contact.html', users =User.objects().order_by('+student_id'))


@contacts_bp.route('/', methods = ['POST'])
def edit():
    user_id = request.form.get('id')
    address = request.form.get('address')
    tel = request.form.get('tel')
    user = User.objects.get(id = user_id)
    user.address = address
    user.tel = tel
    user.save()
    return jsonify({'ok':True})

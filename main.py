# -*- coding: utf-8 -*-
from flask.globals import request
from flask.helpers import url_for
from werkzeug.utils import redirect
from blueprints.contacts import contacts_bp
from jinja_utils import register_filters
from messages import Message
from models import Code
import publish

__author__ = 'yeshiming@gmail.com'

from flask import Flask
from flask import *
app = Flask(__name__, template_folder='template')

@app.route("/")
def index():
    code = request.args.get('code', '')
    if code:
        Code.objects.delete()
        Code.objects.insert(Code(code = code))
        return redirect('http://jaredye.info')
    return render_template('index.html', messages = Message.objects())

@app.route('/post', methods = ('POST',))
def send_message():
    msg = request.form.get('msg')
    return publish.publish(msg) or redirect(url_for("index"))

def register_blueprints():
    app.register_blueprint(contacts_bp, url_prefix = "/contacts")

@app.route('/post-message', methods = ('POST', ))
def post_message():
    content = request.form.get('content')
    Message.objects.insert(Message(content=content))
    return redirect(url_for('index'))

register_blueprints()
register_filters(app)
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)

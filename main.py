# -*- coding: utf-8 -*-
from flask.globals import request
from flask.helpers import url_for
from werkzeug.utils import redirect
from blueprints.contacts import contacts_bp
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
        return redirect('http://wolfware4.com')
    return render_template('index.html')

@app.route('/post', methods = ('POST',))
def send_message():
    print '>>>>'
    msg = request.form.get('msg')

    return publish.publish(msg) or redirect(url_for("index"))

def register_blueprints():
    app.register_blueprint(contacts_bp, url_prefix = "/contacts")

register_blueprints()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)

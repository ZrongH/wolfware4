# -*- coding: utf-8 -*-
from flask.globals import request
from flask.helpers import url_for
from werkzeug.utils import redirect
import publish

__author__ = 'yeshiming@gmail.com'

from flask import Flask
from flask import *
app = Flask(__name__, template_folder='template')

@app.route("/")
def index():
    return render_template('base.html')

@app.route('/post', methods = ('POST',))
def send_message():
    msg = request.form.get('msg')
    publish.publish(msg)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

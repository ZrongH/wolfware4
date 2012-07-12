# -*- coding: utf-8 -*-
from werkzeug.utils import redirect
from models import Code

__author__ = 'yeshiming@gmail.com'

from weibo import APIClient

APP_KEY = '459860685' # app key
APP_SECRET = 'e5233dd415a086d6152ffbbdf755af42' # app secret
CALLBACK_URL = 'http://jaredye.info' # callback url

GET_URL = True



def publish(msg):


#    print msg
    #print url
    code_obj = Code.objects.first()
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    try:
        if code_obj and code_obj.access_token and code_obj.expires_in:
            pass
        else:
            if not code_obj:
                return redirect(client.get_authorize_url())
            r = client.request_access_token(code_obj.code)
            code_obj.access_token = r.access_token # 新浪返回的token，类似abc123xyz456
            code_obj.expires_in = r.expires_in # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
            code_obj.save()

        access_token = code_obj.access_token
        expires_in = code_obj.expires_in

        assert access_token
        print expires_in
        ### TODO: 在此可保存access token
        print "access_token", access_token
        print 'expires_in', expires_in
        client.set_access_token(access_token, expires_in)
        #
        print client.get.statuses__user_timeline()
        print client.post.statuses__update(status=msg)
    except:
        return redirect(client.get_authorize_url())

if GET_URL:
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    url = client.get_authorize_url()
    print url
else:
    publish(u'中午好')

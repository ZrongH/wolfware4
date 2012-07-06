# -*- coding: utf-8 -*-
__author__ = 'yeshiming@gmail.com'

from weibo import APIClient

APP_KEY = '459860685' # app key
APP_SECRET = 'e5233dd415a086d6152ffbbdf755af42' # app secret
CALLBACK_URL = 'http://jaredye.info' # callback url

GET_URL = True



def publish(msg):



    #print url
#    code = "52496a1197a170d403e7346b622ffc4e"

    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
#    r = client.request_access_token(code)
#    access_token = r.access_token # 新浪返回的token，类似abc123xyz456
#    expires_in = r.expires_in # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
    access_token = "2.00CuinJD0plWHV3e39835a195dEQyB"
    expires_in = 1341590474
    print expires_in
    ### TODO: 在此可保存access token
    print "access_token", access_token
    print 'expires_in', expires_in
    client.set_access_token(access_token, expires_in)
    #
    print client.get.statuses__user_timeline()
    print client.post.statuses__update(status=msg)


if GET_URL:
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    url = client.get_authorize_url()
    print url
else:
    publish(u'中午好')

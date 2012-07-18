# -*- coding: utf-8 -*-
import datetime
from flask.globals import request
from flask.helpers import url_for
from flaskext.login import current_user

__author__ = 'yeshiming@gmail.com'

def register_filters(app):

    def url_for_other_page(page):
        """
        :param page:
        :return:
        For pagination
        """
        args = request.view_args.copy()
        args['page'] = page
        return url_for(request.endpoint, **args)

    app.jinja_env.globals['url_for_other_page'] = url_for_other_page

    #
    @app.context_processor
    def inject_user():
        return dict(user=current_user)


    @app.template_filter()
    def timesince(dt, default=u"刚刚"):
        """
        Returns string representing "time since" e.g.
        3 days ago, 5 hours ago etc.
        """

        now = datetime.datetime.now()
        diff = now - dt

        periods = (
            (diff.days / 365, u"年", u"年"),
            (diff.days / 30, u"月", u"月"),
            (diff.days / 7, u"星期", u"星期"),
            (diff.days, u"天", u"天"),
            (diff.seconds / 3600, u"小时", u"小时"),
            (diff.seconds / 60, u"分钟", u"分钟"),
            (diff.seconds, u"秒", u"秒"),
            )

        for period, singular, plural in periods:
            if period:
                return u"%d%s前" % (period, singular if period == 1 else plural)

        return default
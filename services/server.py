# coding: utf-8

from flask import Flask, make_response, request, current_app, jsonify
from datetime import timedelta
from functools import update_wrapper
import requests, rss_sources, news_fetcher, time, sched


# HTTP Access Control script from http://flask.pocoo.org/snippets/56/
def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

app = Flask(__name__)

scheduler = sched.scheduler(time.time, time.sleep)

def print_event(name):
    print 'EVENT:', time.time(), name

x = 5
def updateNews(x):

    re = news_fetcher.fetchNews(x)
    print(re)
    scheduler.enter(2, 1, updateNews, (x,))


scheduler.enter(2, 1, updateNews, (x,))
scheduler.run()

@app.route('/bbc')
@crossdomain(origin='*', headers='Content-Type')
def bbc():
    if 'type' in request.args:
        url = request.args['type']
        googlePrefix = "http://ajax.googleapis.com/ajax/services/feed/load?v=2.0&num=20&callback=JSON_CALLBACK&q="
        url = 'http://feeds.bbci.co.uk/news/rss.xml'
        return resp.text
    else:
        return false


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
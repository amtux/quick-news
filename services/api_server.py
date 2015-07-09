# coding: utf-8

from flask import Flask, make_response, request, current_app, jsonify
from datetime import timedelta
from functools import update_wrapper
from rss_sources import getBbcRss, getCbcRss, getReutersRss
import json


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


@app.route('/bbc')
@crossdomain(origin='*', headers='Content-Type')
def bbc():
    if 'url' in request.args:
        url = request.args['url']
        bbcRss = getBbcRss()
        if url not in bbcRss:
            return jsonify(items="Requested category doesnt exist")
        else:
            directory = "./data/bbc/"
            fileName = url + ".json"
            with open(directory + fileName) as f: 
                s = json.load(f)
            return jsonify(items=s)
    else:
        return jsonify(items="Feed category not defined")

@app.route('/cbc')
@crossdomain(origin='*', headers='Content-Type')
def cbc():
    if 'url' in request.args:
        url = request.args['url']
        cbcRss = getCbcRss()
        if url not in cbcRss:
            return jsonify(items="Requested category doesnt exist")
        else:
            directory = "./data/cbc/"
            fileName = url + ".json"
            with open(directory + fileName) as f: 
                s = json.load(f)
            return jsonify(items=s)
    else:
        return jsonify(items="Feed category not defined")

@app.route('/reuters')
@crossdomain(origin='*', headers='Content-Type')
def reuters():
    if 'url' in request.args:
        url = request.args['url']
        reutersRss = getReutersRss()
        if url not in reutersRss:
            return jsonify(items="Requested category doesnt exist")
        else:
            directory = "./data/reuters/"
            fileName = url + ".json"
            with open(directory + fileName) as f: 
                s = json.load(f)
            return jsonify(items=s)
    else:
        return jsonify(items="Feed category not defined")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',threaded=True)
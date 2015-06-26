# codinsummaries = SummarizeUrl(url)g: utf-8
from flask import Flask, jsonify, request
from pyteaser import SummarizeUrl
import json

app = Flask(__name__)


@app.route('/')
def index():
    return 'Flask is running!'


@app.route('/data')
def names():
	if 'url' in request.args:
		url = request.args['url']
		summaries = SummarizeUrl(url)
		return json.dumps(summaries)
	else:
		return "false"

if __name__ == '__main__':
	app.run(debug=True)

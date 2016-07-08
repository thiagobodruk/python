#!/usr/bin/env python
from flask import Flask, jsonify, request
from crawler import Crawler

app = Flask(__name__)
crawler = Crawler()

app.debug = True

@app.route('/')
def index():
	return 'Hello, World!'
	
@app.route('/search')
def search():
	keyword = request.args.get('w')
	if keyword:
		res = crawler.search(keyword)
	else:
		res = {'message' : 'No keyword sent'}
	return jsonify(res)

if __name__ == '__main__':
	app.run(port=80)
#!venv/bin/python
from flask import Flask, render_template, request, jsonify
import requests, ast

app = Flask(__name__)

@app.route('/')
def root():
    return 'Feeling RESTful-ish.'

@app.route('/get_dat_json')
def uri():
    return render_template('get_dat_json.html')

@app.route('/_callAPI')
def callAPI():
	uri = request.args.get('uri', 0, type=str)
	in_params = request.args.get('params', 0, type=str)
	if len(in_params) > 0:
		message="bad parameters"
		try:
			clean_params = ast.literal_eval(in_params)
			if type(clean_params)!=type({}):
				message="bad param format (dict)"
				raise TypeError('Not a dict')	
		except:
			return jsonify(status='error',message=message)
	else:
		clean_params = {}
	username = request.args.get('username', 0, type=str)
	password = request.args.get('password', 0, type=str)
	r = requests.get(uri,params=clean_params, auth=(username, password))
	if not r:
		return jsonify(status='error',message='bad request')
	return jsonify(response=r.json())

if __name__ == '__main__':
    app.run(host='localhost', port=8000)

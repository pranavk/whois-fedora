from flask import (Flask, render_template, redirect,
					url_for, request, make_response)
import json, requests, pprint

app = Flask(__name__)


def get_saved_data():
	try:
		data =json.loads(request.cookies.get('user'))
	except TypeError:
		data = {}
	return data

@app.route('/')
def index():
    return render_template('index.html', saves=data)

@app.route('/whois', methods=['POST'])
def whois():

#	user = requests.get('https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/{}'.format())

	response = make_response(redirect(url_for('index')))
	data = get_saved_data()
	data.update(dict(request.form.items()))

	response.set_cookie('user', json.dumps(data))

#	responses = pprint.pprint(user.json())
	return response



app.run(debug=True, host='0.0.0.0', port=8000)

#!/usr/bin/env python3
import json
from flask import Flask, render_template, request, redirect
from werkzeug import secure_filename
from googlevision_api import encode_image, make_post_request
import jinja2
import os

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
UPLOAD_PATH = './static/uploaded_imgs/'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_PATH

@app.route('/')
def display_main_page():
	return render_template("upload_file.html")

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		# when submit is clicked(POST)

		# uploaded_file is the image file object that is uploaded from user
		uploaded_file = request.files['file']

		base64_converted_img = encode_image(uploaded_file)
		
		response = make_post_request(base64_converted_img)

		response_json = json.loads(response.text)


		print(response_json["responses"][0]["textAnnotations"][0]["description"])
		result_str = str(response_json["responses"][0]["textAnnotations"][0]["description"]) # now it's a list of dict

		return render_template('result.html', result_str=result_str)
	
	elif request.method == 'GET':
		return 'REQUEST METHOD IS NOT POST'

@app.route('/post', methods=['GET','POST'])
def post():
	if request.method == 'POST':
		return render_template('post.html')
	return render_template('get.html')




if __name__ == '__main__':
	port = int(os.environ.get('PORT', 8000))
	app.run(host='0.0.0.0', port=port,debug=True)

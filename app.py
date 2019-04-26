#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect
from werkzeug import secure_filename
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
		uploaded_file = request.files['file']
		uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'],
										secure_filename(uploaded_file.filename)))
	return render_template('result.html')

@app.route('/post', methods=['GET','POST'])
def post():
	if request.method == 'POST':
		return render_template('post.html')
	return render_template('get.html')


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 8000))
	app.run(host='0.0.0.0', port=port,debug=True)

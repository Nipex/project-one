import os
from flask import Flask, render_template, url_for, request, redirect, \
				abort, session, g, flash
from werkzeug import secure_filename
from flask import send_from_directory

import settings

# App starts here
app = Flask(__name__)
app.config.from_object(settings)
app.debug = True

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/photos')
def photos():
	return render_template('photos.html')

#Function to check if uploaded file exstension is valid
def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/uploaded', methods=['GET', 'POST'])
#Upload function
def upload():
	if request.method == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
		   filename = secure_filename(file.filename)
		   file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		   return redirect(url_for('upload', filename=filename))
	return render_template('upload.html')

@app.route('/upload')
def upload_page():
	return render_template('upload.html')

@app.route('/upload/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME']:
			error = 'Invalid username or password'
		elif request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid username or password'
		else:
			session['logged_in'] = True
			flash('You were logged in')
			return redirect(url_for('upload_page'))
	return render_template('login.html', error=error)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('index'))

if __name__ == "__main__":
	app.run(host="0.0.0.0")
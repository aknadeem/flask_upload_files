import os
import zipfile
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/upload/'

ALLOWED_EXTENSIONS = set(['zip','jpg','jpeg'])

basedir = os.path.abspath(os.path.dirname(__file__))


# app = Flask(__name__, static_folder="build/assets/",  template_folder="build")
app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 mb
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS	


@app.route('/uploadFiles')
def upload_form():
	# return "Hello World!"
	return render_template('upload.html')

@app.route('/uploadFiles', methods=['POST'])
def upload_image():
	# return "Hello World!"

	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']

	if file.filename == '':
		flash('No File selected for uploading')
		return redirect(request.url)

	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		# save file into folder
		file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename))

		# get file name without extionsion
		file_without_ext = filename.split('.')[0]
		file_with_ext = filename.split('.')[1]

		print("nadeem "+ file_with_ext)

		if(file_with_ext == 'zip'):
			# extract zip file
			zip_ref = zipfile.ZipFile(os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename), 'r')
			# save zip file in same folder ofter extract
			zip_ref.extractall(os.path.join(basedir, app.config['UPLOAD_FOLDER']))
			zip_ref.close()


			# delete zip file after extract
			os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename))

		print('upload_image filename: ' + filename)
		flash('Image successfully uploaded and displayed')
		return render_template('upload.html', filename=filename)
	else:
		flash('Allowed file types are -> zip')
		return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='upload/' + filename), code=301)

if __name__ == '__main__':
	# # app.run(host='0.0.0.0', port=80)
	app.config['SECRET_KEY']= "SecretKey"
	app.run(debug=True)
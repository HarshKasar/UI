#from crypt import methods
import flask
import os
from flask import Flask,flash,redirect,render_template,request
from werkzeug.utils import secure_filename
app=Flask(__name__)
app.secret_key="secret key"
app.config['MAX_CONTENT_LENGTH']=16*1024*1024
path=os.getcwd()
UPLOAD_FOLDER=os.path.join(path,'uploads')
if os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
ALLOWED_EXTENSION=set(['txt','jpg','pdf','png','jpeg','gif'])
def allowed_files(filename):
    return '.' in filename and filename.rsplit('.',1) [1].lower() in ALLOWED_EXTENSION
@app.route('/')
def upload_form():
    return render_template('upload.html')
@app.route('/',methods=['POST'])
def upload_file():
    if request.method=='POST':
        if 'file' not in request.files:
            flash('NO FILE PART')
            return redirect(request.url)
        file=request.files['file']
        if file.filename=='':
            flash('No File Selected For Uploading')
            return redirect(request.url)
        if file and allowed_files(file.filename):
            filename=secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            flash('File Successfully Uploaded')
            return redirect('/')
        else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            return redirect(request.url)
if __name__=="__main__":
    app.run(debug=True)           
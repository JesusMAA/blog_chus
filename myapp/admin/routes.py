from flask import Blueprint, render_template, Flask, request
from myapp.models import User, Blog
from myapp.models import db
from base64 import b64encode
from pathlib import Path
import os

admin = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates/admin')



@admin.route('/')
def admin_index():
    return render_template('opcion.html')

@admin.route('/register')
def register():
    return render_template('register.html')

@admin.route('/upload', methods=['POST'])
def upload():
    nameUser = request.form.get('nameUser')
    description = request.form.get('description')
    file = request.files['inputFile']
    file.save(os.path.join('/home/chus/Documentos/Portafolio/flask/hola/myapp/static/images', file.filename))
    rout = 'images/{}'.format(file.filename)
    new_user =User(name=nameUser, description=description, image_dir=rout)
    db.session.add(new_user)
    db.session.commit()
    return 'Saved'

@admin.route('/upload_blog')
def upload_blog():
    return render_template('blog_register.html')

@admin.route('/upload_blog_saved', methods=['POST'])
def upload_blog_saved():
    print(request.files)
    req = request.form
    title = req.get('title')
    blog = req.get('blog')
    rout = '/home/chus/Documentos/Portafolio/flask/hola/myapp/static/images/user'
    file = request.files['inputFile']    
    fileObj = Path(rout)
    if fileObj.is_file():
        os.mkdir(rout)
    file.save(os.path.join('/home/chus/Documentos/Portafolio/flask/hola/myapp/static/images/user', file.filename))
    rout = 'images/user/{}'.format(file.filename)
    new_blog = Blog(title=title, blog_description=blog, image_dir_blog=rout)
    db.session.add(new_blog)
    db.session.commit()
    return 'Save'

"""@admin.route('/image')
def image():
    file_data = FileContents.query.filter_by(name='Captura de pantalla de 2020-04-25 15-43-56.png').first()
    image = b64encode(file_data.data).decode('ascii')
    return render_template('image.html',data=list,image=image)"""
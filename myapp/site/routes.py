from flask import Blueprint, render_template, redirect, url_for
from myapp.models import FileContents, User, Blog
from base64 import b64encode

site = Blueprint('site', __name__, template_folder='templates', static_folder='myapp/static')


@site.route('/')
def index():
    user = User.query.filter_by(id=1).first()
    #blog = Blog.query.filter_by(id=1).first()
    blog = Blog.query.all()
    #print(blog)
    return render_template('index.html', user=user, blog=blog)

@site.route('/<int:number>')
def blog(number):
    user = User.query.filter_by(id=1).first()
    blog = Blog.query.filter_by(id=number).first()
    return render_template('user.html', user=user, blog=blog)

@site.route('/<random>')
def redir(random=None):
    return redirect(url_for('.index'))

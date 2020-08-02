from flask import Blueprint, render_template, redirect, url_for
from myapp.models import FileContents, User, Blog
from base64 import b64encode

site = Blueprint('site', __name__, template_folder='templates/site', static_folder='myapp/static')


@site.route('/')
@site.route('/index')
@site.route('/<int:page>')
@site.route('/index/<int:page>')
def index(page=None):
    user = User.query.filter_by(id=1).first()
    blog = Blog.query.order_by(Blog.id.desc()).paginate(page, 5, False)
    #print(len(blog))
    if len(blog.items)==0:
        return redirect(url_for('.index'))
    return render_template('index.html', user=user, blog=blog)

@site.route('/<int:number>')
def blog(number):
    user = User.query.filter_by(id=1).first()
    blog = Blog.query.filter_by(id=number).first()
    return render_template('user.html', user=user, blog=blog)

@site.route('/<random>')
def redir(random=None):
    return redirect(url_for('.index'))

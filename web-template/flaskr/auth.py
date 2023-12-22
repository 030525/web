import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

# 名字和下列路由的前缀
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/index',methods=(['GET','POST']))
def index():
    if request.method == 'POST':
        a = 1
    
    return render_template('index.html')

@bp.route('/about',methods=(['GET','POST']))
def about():
    if request.method == 'POST':
        a = 1
    
    return render_template('about-us.html')

@bp.route('/contact',methods=(['GET','POST']))
def contact():
    if request.method == 'POST':
        a = 1
    
    return render_template('contact-us.html')

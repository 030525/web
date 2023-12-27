import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db
from flaskr.send import *
from flaskr.email import *
import random
import string

bp = Blueprint('auth', __name__, url_prefix='/auth')


def generate_verification_code():
    # 生成数字和字母的字符集
    characters = string.digits + string.ascii_letters
    # 生成六位验证码
    verification_code = ''.join(random.choice(characters) for _ in range(10))
    return verification_code

@bp.route('/index',methods=(['GET','POST']))
def index():
    if request.method == 'POST':
        if 'email_verify' in request.form:
            email = request.form.get('email')
            
            delete_overtime(email)
            
            if query_exist(email) is False:
                code = generate_verification_code()
                insert_verify_code(email,code)
                send_verify_code(email,code)


    
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

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

# 名字和下列路由的前缀
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/firstpage',methods=(['GET']))
def firstpage():
    if g.user is None:
        return redirect(url_for('auth.login'))
    else:
        return redirect(url_for('home.welcome'))


# get和post触发
@bp.route('/register', methods=('GET', 'POST'))
def register():
    #post时处理
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        id = request.form['identity']
        phone = request.form['phone']


        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not id:
            error = 'Username is required.'
        elif not phone:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (id,phone,username, password) VALUES (?,?,?, ?)",
                    (id,phone,username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"ID {id} or Phone {phone} is already registered."
            else:
                #http重定向到auth蓝图下login函数
                return redirect(url_for("auth.login"))

        #向flash写入错误
        flash(error)

    #渲染模板
    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        phone = request.form['phone']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE phone = ?', (phone,)
        ).fetchone()

        if user is None:
            error = 'Incorrect phone.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            


            return redirect(url_for('home.welcome'))

        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
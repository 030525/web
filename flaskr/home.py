import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db
from datetime import datetime

bp = Blueprint('home', __name__, url_prefix='/home')

@bp.route('/welcome', methods=('GET', 'POST'))
def welcome():
    if request.method == 'POST':
        user_id = session.get('user_id')
        loan_id = request.form['loan_id']

        current_datetime = datetime.now()

        db=get_db()
        db.execute(
            "INSERT INTO who_borrow (id, loan_id, loan_date) VALUES (?,?,?)",
            (user_id, int(loan_id),current_datetime ),
        )
        db.commit()

    id = session.get('user_id')

    rank_fetch = get_db().execute(
            'SELECT rank FROM credit WHERE id = ?', (id,)
        ).fetchone()

    loans_fetch = get_db().execute(
            'SELECT loan_id,loan_type ,amount, interest, repay ,loan_period  FROM loans WHERE rank = ?', (rank_fetch['rank'],)
        ).fetchall()
    loans_data = [dict(row) for row in loans_fetch]

    return  render_template('home/welcome.html',loans=loans_data)




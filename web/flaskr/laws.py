import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db
from datetime import datetime

bp = Blueprint('laws', __name__, url_prefix='/laws')

@bp.route('/submit/<int:loan_id>', methods=('GET', 'POST'))
def submit(loan_id):
    if request.method == 'POST':
        user_id = session['user_id']
        current_datetime = datetime.now()

        db=get_db()
        db.execute(
            "INSERT INTO borrow (id, loan_id, loan_date) VALUES (?,?,?)",
            (user_id, int(loan_id),current_datetime ),
        )
        db.commit()

        borrow_id = db.execute(
            "SELECT borrow_id FROM borrow WHERE id=? AND loan_id=? AND loan_date=?",
            (user_id, int(loan_id), current_datetime)
        ).fetchone()

        borrow_id = int(borrow_id['borrow_id'])
        db.execute("INSERT INTO unpaid (borrow_id) VALUES (?)", (borrow_id,))
        db.commit()

        return redirect(url_for('home.welcome'))

    return  render_template('laws/submit.html')

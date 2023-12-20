import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('my', __name__, url_prefix='/my')

@bp.route('/main', methods=('GET', 'POST'))
def main():
    id = session.get('user_id')
    borrow_fetch = get_db().execute(
            'SELECT strftime("%Y-%m-%d-%H-%M", loan_date) as loan_date,loan_id FROM who_borrow WHERE id = ?', (id,)
        ).fetchall()

    borrow = [dict(row) for row in borrow_fetch]

    result = []

    for pair in borrow:
        loan_id = pair['loan_id']

        ret = get_db().execute(
            'SELECT loan_type ,amount, interest, repay ,loan_period  FROM loans WHERE loan_id = ?', (loan_id,)
        ).fetchone()

        ret = dict(ret)
        ret['loan_date'] = pair['loan_date']

        result.append(ret)

    return  render_template('my/main.html',loans=result)


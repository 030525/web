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

    rank_fetch = get_db().execute(
            'SELECT rank FROM credit WHERE id = ?', (id,)
        ).fetchone()

    loans_fetch = get_db().execute(
            'SELECT loan_type ,amount, interest, repay ,loan_period  FROM loans WHERE rank = ?', (rank_fetch['rank'],)
        ).fetchall()
    loans_data = [dict(row) for row in loans_fetch]

    return  render_template('my/main.html')
    return  render_template('home/welcome.html',loans=loans_data)


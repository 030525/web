from flaskr.db import get_db
import datetime


def query_exist(email):
    db = get_db()
    a = db.execute(
        "select  * from email_verify where email = ?",(email,)
    ).fetchone()

    if a is None:
        return False
    else:
        return True

def insert_verify_code(email,code):
    db = get_db()
    current_time = datetime.datetime.now()
    db.execute(
        "INSERT INTO email_verify (email,verify_code,generate_time) VALUES (?,?,?)",
        (email,code,current_time ),
    )
    db.commit()



def delete_overtime(email,seconds=60):
    current_time = datetime.datetime.utcnow()
    threshold_time = current_time - datetime.timedelta(seconds=seconds)

    db = get_db()
    db.execute("DELETE FROM email_verify WHERE email = ? and generate_time < ?", (email,threshold_time))
    db.commit()

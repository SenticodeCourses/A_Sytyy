from app import app
from flask import render_template
from flask import request
from mongo import MongoDB


@app.route('/<pref>', methods = ['GET', 'POST'],)
def read_update(pref):
    db = MongoDB()
    print(request.method)
    if request.method == 'POST':
        value = request.form['value']
        db.update_db(pref, value)
        user_info = db.get_info(pref)
        return render_template('output.html', pref = pref, user = user_info)

    else:
        user_info = db.get_info(pref)
        return render_template('output.html', pref=pref, user=user_info)
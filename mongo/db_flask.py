import pymongo as pm
from flask import Flask
from flask import request


app_fl = Flask(__name__)

client = pm.MongoClient("localhost", 27017)
db = client.test

print(list(db.somedata.find()))

@app_fl.route('/<pref>', methods = ['GET', 'POST'])
def read_update(pref):
    if request.method == 'POST':
        form = dict(request.form)
        db.somedata.update_one({}, {"$set": {pref: form['name'][0]}})
        user = db.somedata.find_one()
        return '''
                       <!DOCTYPE html>
                   <html lang="en">
                   <head>
                       <meta charset="UTF-8">
                       <title>Title</title>
                   </head>
                   <body>
                       <h1>Your ''' + pref + ' = ' + user[pref] + '''</h1>
                       <form method="post">
               <input type="text" name="name"><br>
               <input  type="submit"  value="Submit">
           </form
                   </body>
                   </html>
                       '''
    else:
        user = db.somedata.find_one()
        return '''
                <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Title</title>
            </head>
            <body>
                <h1>Your ''' + pref + ' = ' + user[pref] + '''</h1>
                <form method="post">
        <input type="text" name="name"><br>
        <input  type="submit"  value="Submit">
    </form
            </body>
            </html>
                '''



app_fl.run('localhost', '8080')
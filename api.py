import bottle
import mysql.connector as connector
import bottle_mysql
from bottle import route, run
from bottle import error
from bottle import response
from bottle import template
from bottle import request
import json
app = bottle.Bottle()
plugin = bottle_mysql.Plugin(dbuser='root', dbpass='', dbname='pythondb')
app.install(plugin)
db = connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pythondb")
mycursor = db.cursor()

def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if bottle.request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors

@route('/show/:item')
@enable_cors
def show(item):
    sql = "SELECT * FROM relics where name ='{}';".format(item)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if myresult:
        myresult = json.dumps(myresult)
        return myresult
    return error404

@route('/insert')
@enable_cors
def insert():
    data = request.get_json()
    name = data['name']
    expansion = data['expansion']
    sql = "INSERT INTO relics (name, expansion) VALUES('{}', '{}');".format(name, expansion)
    mycursor.execute(sql)


@route('/hello')
def hello():
    return "Hello World!"

@error(404)
def error404(error):
    return 'Nothing here, sorry'

run(host='localhost', port=8080, debug=True)
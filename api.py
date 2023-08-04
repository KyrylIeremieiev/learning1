import bottle
import mysql.connector as connector
import bottle_mysql
from bottle import route, run
from bottle import error
from bottle import template
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

@route('/show/:item')
def show(item):
    sql = "SELECT * FROM relics where name ='{}';".format(item)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if myresult:
        myresult = json.dumps(myresult)
        return myresult
    return error404

@route('/hello')
def hello():
    return "Hello World!"

@error(404)
def error404(error):
    return 'Nothing here, sorry'

run(host='localhost', port=8080, debug=True)
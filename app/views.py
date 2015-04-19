#-*-coding:utf8-*-
import MySQLdb
from app import app
from flask import Flask,g,request,render_template

@app.before_request
def before_request():
	g.db = MySQLdb.connect(app.config['MYSQL_HOST'],app.config['MYSQL_USER'],app.config['MYSQL_PASS'],app.config['MYSQL_DB'],app.config['MYSQL_PORT'])

@app.teardown_request
def teardown_request(exception):
	if hasattr(g,'db'):
		g.db.close()

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname':'snow'}
	nav = [{
				'txt':'Home',
				'href':'/index',
				'active':True
			},
			{
				'txt':'About',
				'href':'/about',
				'active':False
			},
			{
				'txt':'Contact',
				'href':'/contact',
				'active':False
			}]	
	return render_template("index.html",title="index page",user = None,nav = nav)

@app.route('/login',methods=["GET","POST"])
def login():
	if request.method == "GET":
		return	render_template("login.html")	

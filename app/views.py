#-*-coding:utf8-*-
import MySQLdb
from app import app
from flask import Flask,g,request,render_template,url_for,redirect,session
from models import User

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
	userinfo = None
	if 'userinfo' in session:
		userinfo = session['userinfo']
	return render_template("index.html",title="index page",userinfo = userinfo,nav = app.config['NAVITEMS'])

@app.route('/login',methods=["GET","POST"])
def login():
	if request.method == "GET":
		return	render_template("login.html")
	elif request.method == 'POST':
		user = User(g.db)
		#validate user id
		userinfo = user.validate(request.form['username'],request.form['password'])
		if userinfo is not None:
			session['userinfo'] = userinfo
			return redirect("index")
		else:
			return 'error username or password'
@app.route('/logout')
def logout():
	if 'userinfo' in session:
		del session['userinfo']

	return redirect(url_for('index'))

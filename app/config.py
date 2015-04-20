#DEBUG CONFIG
debug = True

#SECURE CONFIG
CSRF_ENABLED = True
SECRET_KEY = "this_is_snow's_corner_and_I_am_hulb_snow."

#MYSQL CONFIG
MYSQL_HOST = "localhost"
MYSQL_USER = "snow"
MYSQL_PASS = "snow"
MYSQL_DB = "blogdb"
MYSQL_PORT = 3306

#application config
NAVITEMS = [{
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

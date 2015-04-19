#-*-coding:utf8-*-
class User():
	self.id = -1
	self.username = ""
	self.email = ""
	self.role = -1
	self.token = ""
		

	def isauthenticated(self):
		return self.id>0 and (self.username!="" or self.token!="")

	def  validate(username,passwd,db):
		sql = "select id,username,email,role from users where username = %s and passwd = %s"
		cursor = db.cursor()
		count = cursor.execute(sql,(username,passwd))
		result = cur.fetchall()
		
	

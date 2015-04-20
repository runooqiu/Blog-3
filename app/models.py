#-*-coding:utf8-*-
class User():
	#User  attributes
	attributes = ['id','username','email','role','defines']	

	def __init__(self,db):
		#use database obj initialize class User
		self.db = db	

	def  validate(self,username,passwd):
		sql = "select id,username,email,role,defines from users where username = %s and passwd = %s"
		cur = self.db.cursor()
		#use cur.execute() to post args into sql in case of  sql injection
		count = cur.execute(sql,(username,passwd))
		result = cur.fetchall()
		if len(result)!=1:
			return None
		else:
			#turn sql result with user info into dict
			self.data = {}
			for index,item in enumerate(result[0]):
				self.data[User.attributes[index]] = item
		return self.data

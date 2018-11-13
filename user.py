

class User:
	'''
	Class creates new instance of user class
	'''

	user_list = []

	def __init__(self,username,password):

		self.username = username
		self.password = password

	def save_user(self):
		'''
		Saves new user to the application
		'''

		User.user_list.append(self)

	def delete_user(self):
		'''
		Removes user from the application
		'''

		User.user_list.remove(self)
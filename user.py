

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


	@classmethod
	def find_by_username(cls,username):
		'''
		Finds users using their usernames
		'''

		for user in cls.user_list:
			if user.username == username:
				return user


	@classmethod
	def user_exist(cls,username):
		'''
		Checks if a given user exists
		'''

		for user in cls.user_list:
			if user.username == username:
				return user


	@classmethod
	def display_all_users(cls):
		'''
		Method returns all users list
		'''

		return cls.user_list
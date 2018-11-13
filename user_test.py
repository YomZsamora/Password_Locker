import unittest
from user import User

class TestUser(unittest.TestCase):

	def setUp(self):
		'''
		Set up method to run before each test case
		'''

		self.new_user = User("yomz","@dZumi0991") #  create user object


	def test_init(self):
		'''
		test_init test case to test if new users is instantiated successfully
		'''

		self.assertEqual(self.new_user.username,"yomz")
		self.assertEqual(self.new_user.password,"@dZumi0991")


	def test_save_user(self):
		'''
		test_save_user test case tests whether a new user is successfully saved
		'''

		self.new_user.save_user()
		self.assertEqual(len(User.user_list),1)


	def test_save_multiple_users(self):
		'''
		test case tests whether we can save multiple users
		'''

		self.new_user.save_user()
		test_user = User("samora","Password")
		test_user.save_user()
		self.assertEqual(len(User.user_list),2)


	def tearDown(save_user):
		'''
        tearDown method that does clean up after each test case has run.
        '''

		User.user_list = []


if __name__ == '__main__':
    unittest.main()
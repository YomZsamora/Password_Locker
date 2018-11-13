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


	def test_delete_user(self):
		'''
		Test if we can remove user from User List
		'''

		self.new_user.save_user()
		test_user = User("samora","password")
		test_user.save_user()

		self.new_user.delete_user()
		self.assertEqual(len(User.user_list),1)


	def tearDown(self):
		'''
        tearDown method that does clean up after each test case has run.
        '''

		User.user_list = []


	def test_find_user_by_username(self):
		'''
		Test to find out if we can find user by username and display credentials
		'''

		self.new_user.save_user()
		test_user = User("samora","password")
		test_user.save_user()

		found_user = User.find_by_username("samora")

		self.assertEqual(found_user.password, test_user.password)


	def test_if_user_exists(self):
		'''
		Test to see if a given user exists
		'''

		self.new_user.save_user()
		test_user = User("samora","password")
		test_user.save_user()

		user_exists = User.user_exist("samora")

		self.assertTrue(user_exists)


	def test_display_all_users(self):
		'''
		Test to see if all the saved users are displated
		'''

		self.assertEqual(Contact.display_all_users(),Contact.user_list)




if __name__ == '__main__':
    unittest.main()
#!/usr/bin/env python3.6

from user import User

def create_user(username,password):
	'''
	Function to create new user
	'''

	new_user = User(username,password)
	return new_user


def save_user(user):
	'''
	Function to save new user
	'''

	user.save_user()


def delete_user(user):
	'''
	Function that deletes a user
	'''

	user.delete_user()


def find_user(username):
	'''
	Function that finds a user
	'''

	return User.find_by_username(username)


def check_existing_users(username):
	'''
	Function that checks if a user exists
	'''

	return User.user_exist(username)


def display_users():
	'''
	Function that returns all the saved users
	'''

	return User.display_all_users


def main():
	print("Hello there! This application helps you manage your credentials.")
	print("Please choose what you want to do using the short codes provided.")
	print('\n')

	while True:
		print("Use these short codes : cu - create a new user, du - display users, fu -find a user, ex -exit the user list ")

		short_code = input().lower()



if __name__ == '__main__':

    main()
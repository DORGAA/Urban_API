from dydb import create_item, delete_item, read_item, read_items
from flask_server import logger

table = 'urban-player'


def create_player(mail, name, organiser=None):
	"""
	Adds a player to the table.
	:param mail: player's email
	:param name: player's name
	:param organiser: organiser's flag 
	"""
	player = {
		"mail": mail,
		"name": name,
	}
	if organiser:
		player["organiser"] = True

	return create_item(player, table)


def get_player(mail):
	"""
	gets a player from the table.
	:param mail: player's email
	"""
	key = {'mail': mail}
	response = read_item(key, table)
	status_code = response["ResponseMetadata"]["HTTPStatusCode"]
	if status_code == 200:
		return response["Item"]
	else:
		logger(response)
		return {}


def get_players():
	"""
	get players from the table.
	"""
	return read_items(table)


def delete_player(mail):
	"""
	delete s a player from table
	:param mail: player's email
	"""
	response = delete_item(mail, table)
	# TODO format response and catch error
	return response


def update_player(mail, name=None, organiser=None):
	"""
	update player in the table
	:param mail: player's email
	:param name: player's name
	:param organiser: organiser's flag
	"""
	player = get_player(mail)
	if player:
		response = create_player(mail, name, organiser)
	else:
		response = {}
	return response




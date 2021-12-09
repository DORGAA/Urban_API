import boto3
import json

client = boto3.resource('dynamodb', region_name='eu-west-1')


def read_item(key, table):
	"""
	dynamoDB table
	:param key: element dictionary
	:param table: table name
	"""
	tab = client.Table(table)
	response = tab.get_item(Key=key)
	return response


def read_items(table):
	"""
	read items on dynamoDB table
	:param table: table name
	"""
	tab = client.Table(table)

	response = tab.scan()
	data = response['Items']

	while 'LastEvaluatedKey' in response:
		response = tab.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
		data.extend(response['Items'])
	return str(data)


def create_item(item, table):
	"""
	Create an item on dynamoDB table
	:param item: element dictionary
	:param table: table name
	"""
	tab = client.Table(table)
	response = tab.put_item(Item=item)
	return response


def delete_item(key, table):
	"""
	delete an item on dynamoDB table
	:param key: element dictionary
	:param table: table name
	"""
	tab = client.Table(table)
	response = tab.delete_item(Key=key)
	return response


def update_item(key, table):
	tab = client.Table(table)
	response = tab.update_item(key=key)
	return response



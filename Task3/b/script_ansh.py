import json
import xmltodict
import ast
import pymongo

client = MongoClient("mongodb+srv://<USERNAME>:<PASSWORD>@task3-cluster.yep8d.mongodb.net/<DATABASENAME>?retryWrites=true&w=majority")
db = client.get_database('<DATABASENAME>')

Collection = db["<COLLECTION>"]

file_json = open("test.json", "a+")
file_xml = open("Users.xml")

skip = 0 
for line in file_xml:
	skip = skip + 1
	if skip <= 2:
		continue

	line = xmltodict.parse(line)  
	json_data = json.dumps(line)
	res = ast.literal_eval(json_data)

	keys = []
	for key in res['row'].keys():
		keys.append(key)

	for key in keys:
		res['row'][str(st[1:])] = res['row'].pop(key)

	json_data = json.dumps(res['row'])
	file_json.write(json_data) 
	file_json.write('\n')
	if isinstance(json_data, list): 
		Collection.insert_many(json_data)   
	else: 
		Collection.insert_one(json_data)




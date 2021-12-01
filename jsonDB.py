import json

# Getting the public key of the other person
def getPublicKey(requesterName, filename='./database.json'):

	json_data=open(filename)
	data=json.load(json_data)
	json_data.close()

	for client in data['publicKeys']:
		if client['client'] != requesterName:
			return client['publicKey']

# Database initiation on every server run
def initDB(filename='./database.json'):

	data = {"publicKeys":[]}
	json_object = json.dumps(data)
	with open(filename, "w") as outfile:
		outfile.write(json_object)

# Appending to the json file
def write_json(new_data, filename='./database.json'):

	with open(filename,'r+') as file:
		file_data = json.load(file)
		file_data["publicKeys"].append(new_data)
		file.seek(0)
		json.dump(file_data, file, indent = 4)

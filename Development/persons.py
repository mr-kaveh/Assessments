#!/usr/bin/env python
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
auth = HTTPBasicAuth()

#Setting up Authentication for securing the API
@auth.get_password
def get_password(username):
    if username == 'hossein':
        return 'Task1'
    return None

#Handling Authentication Related Errors
@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

#improve our 404 & 400 error handlers to respond with JSON
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def invalid_type(error):
    return make_response(jsonify({'error': 'INVALID TYPE'}), 400)

#in-memory database of persons,
#in order to store person entities 
persons = [
	{
		"id": 1,
		"first_name": "John",
		"last_name": "Keynes",
		"age": "29",
		"favourite_colour": "red"
	},
	{
		"id": 2,
		"first_name": "Sarah",
		"last_name": "Robinson",
		"age": "54",
		"favourite_colour": "blue"
	}
]

#Generating the full URI for 
#each person instead of id
#to improve the API interface;
def make_public_person(person):
    new_person = {}
    for field in person:
        if field == 'id':
            new_person['uri'] = url_for('get_specific_person', person_id=person['id'])
        else:
            new_person[field] = person[field]
    return new_person

#An example on how to invoke GET HTTP Method
#curl -u hossein:Task1 -i http://localhost:5000/staff/api/v1.0/persons

#get_person() Function URI,
#suitable for the GET HTTP Method.
@app.route('/staff/api/v1.0/persons', methods=['GET'])
@auth.login_required
def get_person():
	return jsonify({'tasks': map(make_public_person, persons)})

#get_specific_person() Function
#to get each person info by id
@app.route('/staff/api/v1.0/persons/<int:person_id>', methods=['GET'])
@auth.login_required
def get_specific_person(person_id):
    person = [person for person in persons if person['id'] == person_id]
    if len(person) == 0:
        abort(404)
    return jsonify({'specific_person': person[0]})

#An example on how to invoke POST HTTP Method
#curl -u hossein:Task1 -i -H "Content-Type: application/json" -X POST -d '{"first_name":"Mic","last_name":"Blue","age":"35","favourite_colour":"blue"}' http://localhost:5000/staff/api/v1.0/persons

#add_person() Function URI
#suitable for the POST HTTP Method.
@app.route('/staff/api/v1.0/persons', methods=['POST'])
@auth.login_required
def add_person():
    if not request.json:
        abort(400)
    person = {
	'id': persons[-1]['id'] + 1,	#the new id would be the id of the last person plus one
        'first_name': request.json['first_name'],
        'laste_name': request.json['last_name'],
        'age': request.json['age'],
        'favourite_colour': request.json['favourite_colour']
    }
    persons.append(person)
    return jsonify({'person': person}), 201

#an example on how to invoke PUT HTTP Method
#curl -i -H "Content-Type: application/json" -X PUT -d '{"age":"36"}' http://localhost:5000/staff/api/v1.0/persons/2
@app.route('/staff/api/v1.0/persons/<int:person_id>', methods=['PUT'])
@auth.login_required
def update_person(person_id):
    person = [person for person in persons if person['id'] == person_id]
    if len(person) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'first_name' in request.json and type(request.json['first_name']) is not unicode:
        abort(400)
    if 'last_name' in request.json and type(request.json['last_name']) is not unicode:
        abort(400)
    if 'age' in request.json and type(request.json['age']) is not unicode:
        abort(400)
    if 'favorite_colour' in request.json and type(request.json['favorite_colour']) is not unicode:
        abort(400)
    person[0]['first_name'] = request.json.get('first_name', person[0]['first_name'])
    person[0]['last_name'] = request.json.get('last_name', person[0]['last_name'])
    person[0]['age'] = request.json.get('age', person[0]['age'])
    person[0]['favourite_colour'] = request.json.get('favourite_colour', person[0]['favourite_colour'])
    return jsonify({'person': person[0]})

#an example on how to invoke DELETE HTTP Method
#curl -u hossein:Task1 -X "DELETE"  http://localhost:5000/staff/api/v1.0/persons/2
@app.route('/staff/api/v1.0/persons/<int:person_id>', methods=['DELETE'])
@auth.login_required
def delete_person(person_id):
    person = [person for person in persons if person['id'] == person_id]
    if len(person) == 0:
        abort(404)
    persons.remove(person[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)


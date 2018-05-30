# Problem #1

simple RESTful API which provides a service for storing, updating,retrieving and deleting Staff members

## Getting Started

Bellow is a set of instructions along with a copy of the project, which will guide you for preparing the environment as well as running it on your local machine for development and testing purposes.


### Prerequisites

The project is developed on a Centos 7 machine with the following tools Set up:

```
Python
Flask
Flask-Restful
flask-jsonpify

```

### Installing

Centos 7 comes with Python2.7 which is sufficient for our project. in order to use python3 you must install 'epel' repository.

Setting up our environment:

```
yum install python-pip
```

Update pip and install virtualenv:

```
pip install -U pip
pip install -U virtualenv
```
to create a project from scratch you may do the rest in the project directory.my project directory was '~/Assessments/Development'.

```
virtualenv venv
source venv/bin/activate
pip install flask flask-jsonpify flask-restful
pip freeze

```

## GET , POST , PUT and DELETE using the API

since, The 4 Substantial Methods of API is protected with a basic Authentication Method, every request should be accompanied by a User/Password set.

An example on how to invoke GET HTTP Method

```
#curl -u hossein:Task1 -i http://localhost:5000/staff/api/v1.0/persons
```

An example on how to invoke POST HTTP Method

```
#curl -u hossein:Task1 -i -H "Content-Type: application/json" -X POST -d '{"first_name":"Hossein","last_name":"Davoodi","age":"30","favourite_colour":"Green"}' http://localhost:5000/staff/api/v1.0/persons
```
an example on how to invoke PUT HTTP Method

```
#curl -u hossein:Task1 -i -H "Content-Type: application/json" -X PUT -d '{"age":"36"}' http://localhost:5000/staff/api/v1.0/persons/2
```
an example on how to invoke DELETE HTTP Method
```
#curl -u hossein:Task1 -X "DELETE"  http://localhost:5000/staff/api/v1.0/persons/2
```

## 

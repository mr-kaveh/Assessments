# Assesments

Development and Operation Tests. i was supposed to complete 2  problems out of 4,
but i ended up completing 3 tests, which was kind of fun.

# Development Assesment

Problem #1 was solved and pushed to the Development Directory.

## problem #1 of Dev

Create a simple RESTful API which provides a service for storing, updating,
retrieving and deleting Person entities such as those represented in the
JSON below:

```
{
"person": [
{
	"first_name": "John",
	"last_name": "Keynes",
	"age": "29",
	"favourite_colour": "red"
},
{
	"first_name": "Sarah",
	"last_name": "Robinson",
	"age": "54",
	"favourite_colour": "blue"
}
]
}
```

# Operation Assesments

Desinging of the Operation Problems was so smart,and after doing some research on both problems
i figured out that both of them can be done by the same set of Tools.this Assesments are pushed into 
the Operation Derectory.

## Problem #1 of Ops

We want to store the access logs of any HTTP server of your choosing (e.g.
httpd, Nginx, lighttpd) in a database. Ideally, a new record should be
created each time there is a new line in the access log. Feel free to use any
logging framework/module and database you want to implement your
solution.

## Problem #2 of Ops

We want to store some metrics of a running server; CPU utilisation, free
memory and disk space to be specifc. We would like to be able to inspect
the collected metrics but it is entirely up to you to provide a method of
doing that. The method could be; going over text fles, logs or database
records, making calls to an exposed API, using a graphical user interface to
display the metrics, running a script to list the metrics on the command line
and anything else you can provide as a minimum viable product. Bear in
mind that you can freely use any third party software for this.

Also assume that this is a development server under load in which the
developers are doing a variety of tasks, like running database and web
servers, transferring fles, opening sockets and exposing ports to the outside
world. What would you additionally monitor to make their life easier and
debug the problems they might be having more efficiently?


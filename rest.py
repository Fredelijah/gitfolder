#RESTFUL

# representational state transfer# structures a pattern for the end user and server to communicate over a network.
#REST constraints
#stateless
#client server
#cacheable
#uniform interface
#layered system    through proxy
#code on demand





# JSON data format use curly braces
#{"name: Fred", "age:23"}
#YAML, XML,SOAP

#HTTP methods
#GET get data or retrieve existing resource
#POST create a new resource
#PUT update a resource
#PATCH partially update a resource
#DELETE delete a resource


#STATUS CODES
#200 ok successful
#201 resource was created
#202 accepted request receive and no modification made
#204 no content, request successful, response has no content
#400 bad request, request malformed
#404 not found, requested resource not found
#500 internal server error when processing request

# write first program

import requests
import json
response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.json())


#POST method

#{
 #   "user id": 1,
 #   "id":1
  #  "title": "python class"
 #   "body": "This is a python class"
#}



import requests
post_url ="https://jsonplaceholder.typicode.com/posts"
post = {"userid":1, "id":101, "title": "RESTFul API", "body": "This is a python class"}
response = requests.post(post_url, json=post)
response.json()
# PUT to update resource
{
    "userId": 1,
    "id": 101,

}
#response = requests.put(post_url, json=post)
#response.json()

#DELETE POST
#response = requests.delete(post_url)
#print(response.json())



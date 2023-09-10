# API
Playground for API dev.

################################################

Curl Commands to access the PUT, POST and DELETE 

-X : Specifies the HTTP request type 

-H : Header type 

-d : data 

For "POST" :
    curl -X POST -H "Content-Type: application/json" -d '{"name": "Item 4"}' http://localhost/...


For "PUT" :
    curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Item"}' http://localhost:5000/api/items/1


For "DELETE" :
    curl -X DELETE -H "Content-Type: application/json" -d '{"name": "Updated Item"}' http://localhost/api/items/1
#################################################
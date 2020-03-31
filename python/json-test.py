import json

# convert from JSON  to Python

x = '{"name":"John", "age":30, "city":"New York"}'

#parse x
y = json.loads(x)
print(y["age"])

# convert from Python to JSON  

x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

y =  json.dumps(x)
print(y)
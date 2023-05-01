#json stands for Javascript object notation , its a human readable lightweight data  interchange format , a syntax for storing and exchanging data, it is commonly
#used for transferring data in web applications , In simple words JSON is a language independent data format, JSON values can be one of the six data types
# strings , numbers, objects , arrays, boolean , null
#How to use JSON in python : Python has built in package called json , which can be used to work with json data

#parsing json data

import json
person_json = '{"name":"kuldeep","age":36 , "city":"Noida"}'
#parse x
person_object= json.loads(person_json)
print("persons name is:", person_object["name"])
print("persons age is ", person_object["age"])

# complete json example with different data type
y = {
    "name": "Kuldeep",
     "age": 36,
     "married": True,
     "Children": 2,
     "cars": [
         {"model":"XUV500"},
     ]

}

print("Json example with different data type", json.dumps(y))
print("Data type of json dump", type(json.dumps(y)))
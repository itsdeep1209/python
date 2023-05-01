#using the request module we can make requests to any web page easily, the http request returns a response object with all the response data (content , coding , status)
# the http request returns a response object with all the response data , request module supports below method.
# get(url , params , args): sends a get request to the specified URL.
# head(url, args):  sends a head request to the specified url
#post(url,data,json,args): send a post request to the specified url
# put(url , data, args): sends a put request to the specified url
#patch(url, data , args ): sends a patch request to the specified url
#delete(url, args): sends a delete request to the url
#request(method, url,args)

import requests
x = requests.get('https://httpbin.org/get')
print(x.text)
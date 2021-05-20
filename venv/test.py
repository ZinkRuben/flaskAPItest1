# importing the requests library
import requests

# defining the api-endpoint
API_ENDPOINT = "http://127.0.0.1:8080/lang/"


# data to be sent to api
data = {'name': "C++"}

# sending post request and saving response as response object
r = requests.post(url=API_ENDPOINT, data=data)
print(r)
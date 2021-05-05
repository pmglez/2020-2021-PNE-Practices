import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMETERS = "?content-type=application/json"

print("Server: " + SERVER)
print("URL: " + SERVER + ENDPOINT + PARAMETERS)

connection = http.client.HTTPConnection(SERVER)
connection.request("GET", ENDPOINT + PARAMETERS)
response = connection.getresponse()
# print(response)
decoded_answer = response.read().decode()
# print(decoded_answer, type(decoded_answer))
dict_response = json.loads(decoded_answer)
# print(dict_response, type(dict_response))

if dict_response["ping"] == 1:
    print("Response received!:", response.status, response.reason)
    print()
    print("PING OK! The database is running")
else:
    print("The database is down!")

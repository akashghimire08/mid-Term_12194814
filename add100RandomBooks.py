 #!/usr/bin/env python3

import requests
import json
from faker import Faker


APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"

def getAuthToken():
    authCreds = (LOGIN, PASSWORD)
    r = requests.post(
        f"{APIHOST}/api/v1/loginViaBasic", 
        auth = authCreds
    )
    if r.status_code == 200:
        return r.json()["token"]
    else:
        raise Exception(f"Status code {r.status_code} and text {r.text}, while trying to Auth.")

def addBook(book, apiKey):
    num=str(id)
    r = requests.post(
        f"{APIHOST}/api/v1/books", 
        headers = {
            "Content-type": "application/json",
            "X-API-Key": apiKey
            },
        data = json.dumps(book)
    )
    if r.status_code == 200:
        print(f"Book {book} added.")
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}, while trying to add book {book}.")
        
        
def delBook(book, apiKey,id):
    id=str(id)
    r = requests.delete(
        f"{APIHOST}/api/v1/books/id", 
        headers = {
            "Content-type": "application/json",
            "X-API-Key": apiKey
            },
        data = json.dumps(book)
    )
    if r.status_code == 200:
        print(f"Book {book} deleted.")
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}, while trying to add book {book}.")
        
# Get the Auth Token Key
apiKey = getAuthToken()

# Using the faker module, generate random "fake" books
fake = Faker()
for i in range(5):
    # add the new random "fake" book using the API
    delBook(book, apiKey,id) 
    
 for i in range(-5,-1): 
    delBook(book, apiKey,id)  

import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response=requests.get(self.url) #sends a get request to the url and stores the resonse  in a variable called response
        return response.content #.content is the raw response body as bytes ,not yet parsed

    def load_json(self):
        return json.loads(self.get_response_body())
        #fetch the raw body then converts the json text into pyhton data
        #(json objects become dicts json arrays become lists)
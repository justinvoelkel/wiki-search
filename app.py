import requests
import json
from flask import Flask,request
from flask_hal import HAL,document,link
from urllib.parse import quote

app = Flask(__name__)
HAL(app)
app.config['SERVER_NAME'] = 'wiki-search.com'

@app.route('/', subdomain="<term>")
def search(term):
    search_results = search_wiki(term)
    collection = link.Collection()

    for result in search_results['query']['pages'].values():
        collection.append(link.Link(result['title'], result['fullurl']))
    
    response = document.Document(
        embedded={
            "results": document.Embedded(
                links=collection
            )    
        },
        data={
            "term": term,
        },
    )

    return response.to_json()

def search_wiki(term):
    session = requests.Session()

    BASE_URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "titles": term,
        "generator": "links",
        "gplnamespace": 0,
        "gpllimit": "max",
        "format": "json",
        "prop": "info",
        "inprop": "url"
    }

    response = session.get(url=BASE_URL, params=PARAMS)
    return response.json()
# Wiki Search API
This is a very small Flask application that can be used to retrieve links from wikipedia based on a given search term.

## Getting Started
1. Pull this repository
2. Create virtual environment -- $ python3 -m venv venv
3. Activate virtual environment -- $ . venv/bin/activate
4. Install requirements -- $ pip install -r requirements.txt
5. Run Flask -- $ flask run

## Host Name
The excercise references the domain wiki-search.com so it will need to be added to the machine's hosts file

```
$ echo "127.0.0.1 wiki-search.com" >> /etc/hosts
```

## Making a Request
As noted in the excercise I used curl to mimic the subdomain for testing

```
$ curl -H "Host: dogs.wiki-search.com" 127.0.0.1:5000 | json_pp
```

## Response Formatting
Responses are formatted in the [HAL spec](https://apigility.org/documentation/api-primer/halprimer) as it was similar to the output examples in the excercise gist.

Example response for 'dogs'

```javascript
{
   "term" : "dogs",
   "_embedded" : {
      "results" : {
         "_links" : {
            "Dog" : {
               "href" : "https://en.wikipedia.org/wiki/Dog"
            }
         }
      }
   },
   "_links" : {
      "self" : {
         "href" : "http://dogs.wiki-search.com/"
      }
   }
}
```
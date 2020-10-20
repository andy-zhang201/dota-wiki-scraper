import requests
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get_url(url):
    try:   
        # with environment Requires a context manager. By calling closing() you provide it with a way to close it after.
        with closing(requests.get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
            
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    """
    Returns True if the response seems to be HTML or JSON, False otherwise.
    """
    #Headers is a method in requests library
    content_type = resp.headers['Content-Type'].lower()
    
    return (resp.status_code == 200   # Returns true if the website is online and available (statuscode=200)
    #Returns true if content_type exists
            and content_type is not None
    #Returns true if it is an html document or a json document.
            and (content_type.find('json') > -1 or content_type.find('html')))


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)
# Tests to request html and Json pages. the wikimedia one uses rest api to count pageviews about the wikipedia article about Carl Gauss.
# a = simple_get_url("https://www.dota2.com/international/battlepass")
# b = simple_get_url("https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/all-agents/Carl_Friedrich_Gauss/monthly/20200101/20200601")
# Math: https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/all-agents/Carl_Friedrich_Gauss/monthly/20200101/20200601
# print(b)
# print(a)

c = simple_get_url("https://dota2.gamepedia.com/Dota_2_Wiki")
match_id = 5482502874
# Returns a response object
dota = simple_get_url("https://api.opendota.com/api/matches/%s"%match_id)

r= requests.get("https://api.opendota.com/api/matches/%s"%match_id)
# if c != None:
#     src = c

# # Create a soup object to do stuff with the html page.
# soup = BeautifulSoup(src,"lxml")
# .json() decodes json into a dict object.
jstring = r.json()
print(type(jstring))

# Print match id
# print(jstring["match_id"])

print(jstring["players"][0])


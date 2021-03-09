import requests 
from hashlib import md5 
from bs4 import BeautifulSoup
import mechanicalsoup
#takes data and encoding 
def hash(token, encoding='utf-8'):
    #ms5 function takes token encodes it with utf 8 and spits out the hex digested version
    return md5(token.encode(encoding)).hexdigest()


url = 'http://docker.hackthebox.eu:32012/'




def hasher(url):
    browser = mechanicalsoup.StatefulBrowser()
    op_ses = browser.open(url)
    print(op_ses.text)
    soup = BeautifulSoup(op_ses.text, 'html.parser')
    token = soup.h3.get_text()
    print(token)
    form = browser.select_form("form[action='']")
    hash_t = hash(token)

    browser["hash"] = hash_t 
    response = browser.submit_selected()
    print(response.text)
    return response.text


hasher(url)
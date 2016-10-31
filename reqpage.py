import requests
from bs4 import BeautifulSoup


def findpid(url):
    """ Function that recive a url of facebook page and
    find his id using the web: findmyfbid.com.
    Parameters:
        `url`: string type, url to find.
        return: string type, id of face page. """
    
    # setting headers and url to open
    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {'url':url}
    baseurl="http://findmyfbid.com/"
    session = requests.Session()
    response=session.post(baseurl, headers=headers, data=payload)

    # set up beautifulsoup to find de id in the url response
    soup=BeautifulSoup(response.text,"html.parser")
    #code = soup.find_all('code').getText()
    #print(response.text)#debug
    # find the code tag, get text and finally return it
    #code = soup.code.getText()
    return soup.code.getText()
    #print(code)#debug

if __name__ == "__main__":
    print(findpid("https://www.facebook.com/fotoclubcordoba.oficial"))
    print(findpid("https://www.facebook.com/mariafernanda.barreno"))

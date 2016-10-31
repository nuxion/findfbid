import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}
payload = {'url':'https://www.facebook.com/fotoclubcordoba.oficial'}

session = requests.Session()
response=session.post("http://findmyfbid.com/", headers=headers, data=payload)
soup=BeautifulSoup(response.text,"html.parser")
print("here")
#code = soup.find_all('code').getText()
code = soup.code.getText()
print(code)
#print(response.text)

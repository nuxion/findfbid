import requests

headers = {'User-Agent': 'Mozilla/5.0'}
payload = {'url':'https://www.facebook.com/fotoclubcordoba.oficial'}



session = requests.Session()
response=session.post("http://findmyfbid.com/", headers=headers, data=payload)
print (response.text)

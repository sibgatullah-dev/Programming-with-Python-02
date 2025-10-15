import requests
import os
import webbrowser as web

url = "https://www.codexzo.com"
response = requests.get(url)

fp = open("codexzo.html",'w')
fp.write(response.text)

path = os.path.realpath("codexzo.html")
print(path)
web.open("file://"+path)
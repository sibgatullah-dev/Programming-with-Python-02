import requests
url = "https://dimikcomputing.com"
response = requests.get(url)

fp = open("dimik.html",'w')
fp.write(response.text)
import requests
url = "https://codexzo.com"
response = requests.get(url)
print(type(response))
print(response.ok)# True
print(response.status_code) # is the status code is 200 then everything is ok 
print(response.reason)# OK

# If we make mistakes in the url then the response will be not found 
response = requests.get("https://example.com/abc.html")
print(response.ok)# False
print(response.status_code)# 404
print(response.reason)# NOT FOUND
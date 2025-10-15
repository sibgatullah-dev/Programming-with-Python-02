import requests
import sys

url = sys.argv[1]
file = sys.argv[2]
r = requests.get(url)

with open(file,'wb') as f:
    f.write(r.content)
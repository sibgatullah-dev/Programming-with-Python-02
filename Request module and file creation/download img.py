import requests

img_url = 'https://img.freepik.com/premium-photo/abstract-landscape-with-sun-plants_1326522-29843.jpg' # change the url and download different images for free 

r = requests.get(img_url)

with open('walpaper1.jpg','wb') as f:# if we used write(w) method we would need to pass str since we are getting an image which is byte
    f.write(r.content)# so we need write binary(wb) method and the write command is r.content 
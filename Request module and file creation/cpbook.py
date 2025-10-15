import requests
import sys

base_url = 'https://subeen.com/download/'

info_dt = {
    'name': 'Subeen',
    'email': 'book@subeen.com',   # <-- fixed email
    'country': 'Bangladesh'
}

url = base_url + 'process.php'

response = requests.post(url, data=info_dt)

if not response.ok:
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    sys.exit("Error downloading the file.")# we can exit from anywear from the program by using the exit() function of system module 

with open('cpbook.pdf', 'wb') as fp:  # <-- fixed mode
    fp.write(response.content)

print("Book download complete!")

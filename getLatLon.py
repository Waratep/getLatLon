import requests
import json
url = 'https://ipaddress.my/'
r = requests.get(url)
a = r.content.decode()
x = a.split('\n')

count = 0
for i in x:
    if i == '<td>Latitude:</td>':
        buf = x[count + 1].replace('<td>','')
        buf = buf.replace('</td>','')
        print('lat',buf)
    
    elif i == '<td>Longitude:</td>':
        buf = x[count + 1].replace('<td>','')
        buf = buf.replace('</td>','')
        print('lon',buf)
        
    count += 1



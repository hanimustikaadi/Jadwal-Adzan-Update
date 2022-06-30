import requests
from bs4 import BeautifulSoup

content = requests.get('https://kalam.sindonews.com/jadwalsholat')


soup = BeautifulSoup(content.text, 'html.parser')
title = (soup.find('title')).text
print(title)


result= soup.find('tr',{'class':'current-date'})
result= result.findChildren('td')


i=0
for res in result:
    print(i , res)
    i=i+1


hasil = dict()
hasil['Tanggal'] = result[0].text
hasil['Subuh'] = result[1].text
hasil['imsak'] = result[2].text
hasil['dhuhur'] = result[3].text
hasil['ashar'] = result[4].text
hasil['magrib'] = result[5].text
hasil['isya'] = result[6].text

print('Update Adzan Untuk DKI Jakarta Sekitarnya')
print(f'Tanggal Hari Ini { hasil["Tanggal"]}')
print(f'Waktu imsak { hasil["imsak"]}')
print(f'Waktu Adzan Subuh { hasil["Subuh"]}')
print(f'Waktu Adzan dhuhur { hasil["dhuhur"]}')
print(f'Waktu Adzan ashar { hasil["ashar"]}')
print(f'Waktu Adzan magrib { hasil["magrib"]}')
print(f'Waktu Adzan isya { hasil["isya"]}')


















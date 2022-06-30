import requests
from bs4 import BeautifulSoup


def ekstraksi_data():

    try:
        content= requests.get('https://kalam.sindonews.com/jadwalsholat')
    except Exception:
        return None
    if content.status_code == 200:

       soup = BeautifulSoup(content.text, 'html.parser')
       title = (soup.find('title')).text
       result= soup.find('tr',{'class':'current-date'})
       result= result.findChildren('td')

       hasil = dict()
       hasil['Tanggal'] = result[0].text
       hasil['Subuh'] = result[1].text
       hasil['imsak'] = result[2].text
       hasil['dhuhur'] = result[3].text
       hasil['ashar'] = result[4].text
       hasil['magrib'] = result[5].text
       hasil['isya'] = result[6].text
       return hasil
    else:
        return None

def tampilkan_data(result):

    if result is None:
        print('Tidak bisa menemukan jadwal Adzan Solat')
        return

    print('Update Adzan Untuk DKI Jakarta Sekitarnya')
    print(f'Tanggal Hari Ini { result["Tanggal"]}')
    print(f'Waktu imsak { result["imsak"]}')
    print(f'Waktu Adzan Subuh { result["Subuh"]}')
    print(f'Waktu Adzan dhuhur { result["dhuhur"]}')
    print(f'Waktu Adzan ashar { result["ashar"]}')
    print(f'Waktu Adzan magrib { result["magrib"]}')
    print(f'Waktu Adzan isya { result["isya"]}')

if __name__ == '__main__':

    result = ekstraksi_data()
    tampilkan_data(result)


















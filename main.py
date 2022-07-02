import requests
from bs4 import BeautifulSoup


class AdzanUpdate:
        def __init__(self):
            self.description = 'To get the latest Adzan Schedule in Jakarta'
            self.result = None

        def ekstraksi_data(self):

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
               self.result = hasil
            else:
                return None

        def tampilkan_data(self):

            if self.result is None:
                print('Tidak bisa menemukan jadwal Adzan Solat')
                return

            print('Update Adzan Untuk DKI Jakarta Sekitarnya')
            print(f'Tanggal Hari Ini { self.result["Tanggal"]}')
            print(f'Waktu imsak { self.result["imsak"]}')
            print(f'Waktu Adzan Subuh { self.result["Subuh"]}')
            print(f'Waktu Adzan dhuhur { self.result["dhuhur"]}')
            print(f'Waktu Adzan ashar { self.result["ashar"]}')
            print(f'Waktu Adzan magrib { self.result["magrib"]}')
            print(f'Waktu Adzan isya { self.result["isya"]}')

        def run(self):
            self.ekstraksi_data()
            self.tampilkan_data()

if __name__ == '__main__':
    JadwalAdzan = AdzanUpdate()
    print('Description Package', JadwalAdzan.description )
    JadwalAdzan.run()



















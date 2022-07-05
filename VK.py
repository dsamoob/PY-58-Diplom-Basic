import requests
import time
from tqdm import tqdm


class Vk:
    def __init__(self, token, vk_id):
        self.token = token
        self.vk_id = vk_id

    def _getting_photo_data(self, offset=0, count=200, method=None, album_id=None):
        url = f'https://api.vk.com/method/{method}'
        params = {'owner_id': self.vk_id,
                  'access_token': self.token,
                  'v': 5.131,
                  'extended': 1,
                  'offset': offset,
                  'count': count,
                  'album_id': album_id
                  }
        response = requests.get(url, params=params)
        return response.json()

    def _listing_photos(self, method=None, album_id=None, ):
        i = 0
        count = self._getting_photo_data(method=method, album_id=album_id, offset=i)['response']['count']
        photo_list = {}
        photo_name_checking = {}
        while i < count:
            response = self._getting_photo_data(method=method, album_id=album_id, offset=i)
            for photo in tqdm(response['response']['items']):
                if photo['likes']['count'] not in photo_name_checking:
                    photo_name_checking[photo['likes']['count']] = 0
                    name_of_dict = str(photo['likes']['count'])
                    photo_list[name_of_dict] = \
                        {'likes': photo['likes']['count'],
                         'type': photo['sizes'][-1]['type'],
                         'url': photo['sizes'][-1]['url']}
                    photo_name_checking[photo['likes']['count']] += 1
                    time.sleep(0.1)
                else:
                    name_of_dict = str(photo['likes']['count'])
                    photo_name_checking[photo['likes']['count']] += 1
                    photo_list[f"{name_of_dict}({photo_name_checking[photo['likes']['count']] + 1})"] = \
                        {'likes': photo['likes']['count'],
                         'type': photo['sizes'][-1]['type'],
                         'url': photo['sizes'][-1]['url']}
                    time.sleep(0.01)
            i += 200
        else:
            print('Photos list is ready')
            return photo_list

    def get_albums(self) -> dict:
        albums = {}
        total_photos = self._getting_photo_data(method='photos.getAll')['response']['count']
        response = self._getting_photo_data(method='photos.getAlbums')
        for i in response['response']['items']:
            albums[i['title']] = {'id': i['id'], 'photo_quantity': i['size']}
        for number in range(-7, -5):
            response = self._getting_photo_data(method='photos.get', album_id=number)
            albums[str(number)] = {'id': number, 'photo_quantity': response['response']['count']}
        print(f'Quantity of albums: {len(albums)}\n'
              f'Quantity of photos: {total_photos}')
        return albums

    def all_photos(self) -> dict:
        return self._listing_photos(method='photos.getAll')

    def all_photos_from_album(self, album_id: int) -> dict:
        return self._listing_photos(method='photos.get', album_id=album_id)

    def downloading_all_photos(self, path_for_files):
        photos = self.all_photos()
        for photo in photos.values():
            with open(f'{path_for_files} {photo["name"]}.jpg', 'wb') as file:
                file.write(photo['url'].content)
                time.sleep(0.1)

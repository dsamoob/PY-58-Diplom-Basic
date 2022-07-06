from VK import Vk
from Yandex import YandexDisk
from pprint import pprint

vk_id = int()
token_vk = str()
token_yandex = str()
album_id = int()
album_name = str()


if __name__ == '__main__':
    vk = Vk(token_vk, vk_id)
    ya = YandexDisk(token_yandex)
    photos = vk.all_photos()
    pprint(photos)
    albums = vk.get_albums()
    pprint(albums)
    photos_from_any_album = vk.all_photos_from_album(album_id=int)
    pprint(photos_from_any_album)
    result = ya.bu_all_photos_to_disk(photos_from_any_album, quantity=5, album_name=str )
    pprint(result)

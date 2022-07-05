from VK import Vk
from Yandex import YandexDisk
from pprint import pprint

app_id = ''
vk_id = ''
token_vk = ''
token_yandex = ''


if __name__ == '__main__':
    vk = Vk(token_vk, vk_id)
    ya = YandexDisk(token_yandex)
    photos = vk.all_photos()
    pprint(photos)
    pprint(vk.get_albums())
    result = vk.all_photos_from_album(221697831)
    print(ya.bu_all_photos_to_disk(result, quantity=12, album_name='Dondurmarmaris'))


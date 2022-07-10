from VK import Vk
from Yandex import YandexDisk
from pprint import pprint

vk_id = ''
token_vk = ''
token_yandex = ''


if __name__ == '__main__':
    vk = Vk(token_vk, vk_id)
    ya = YandexDisk(token_yandex)
    photos = vk.all_photos()  # Получение списка(словаря) всех фотографий указанного пользователя
    result = ya.bu_all_photos_to_disk(photos, album_name='123', quantity=7)  # Загрузка фотографий на яндекс диск без
    # указания альбома. Quantity - по умолчанию стоит 5, можно поменять. Также можно добавить album_name='любое
    # название' - для создания папки на диске, если не буджет указана - будет использоваться для названия папки -
    # текущая дата
    albums = vk.get_albums()  # Получение списка(словаря) альбомов пользователя
    photos_from_album = vk.all_photos_from_album(album_id='-7')  # Получение списка(словаря) фотографий из
    # конкретного альбома, необходимо указать ID альбома из полученного ранее списка.

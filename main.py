from VK import Vk
from Yandex import YandexDisk
from pprint import pprint

app_id = '8204777'
vk_id = 3064783
token_vk = 'vk1.a.l1tlvT_HWRowkGGKog-JEADIYVmxRkEd8H5771nzAljrAzoPqACywkYjZvJXpgXZ0z2YeQkIc-VqlQzlNzDRk_DghMJBEiGEziFc6Jniqis_xl4u-6YeevhN8CcMwcLcSMCY-mO8HhhoZhQ1aajb3bZMdqcrOoMi4mK_B3WhxCbWBYZB0nP4CFzceJpp7c1g'
path_for_files = '/Users/egorbelov/GitHub/VK/Images/'
token_yandex = 'AQAAAAAyqgthAADLW0gnrCKtmEMavslB-SnP9nw'


if __name__ == '__main__':
    vk = Vk(token_vk, vk_id)
    ya = YandexDisk(token_yandex)
    # photos = vk.all_photos()
    # pprint(photos)
    pprint(vk.get_albums())
    result = vk.all_photos_from_album(221697831)
    print(ya.bu_all_photos_to_disk(result, quantity=12, album_name='Dondurmarmaris'))
    # ya.make_new_directory(f'/{str(datetime.now()).split()[0]}')






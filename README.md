# PY-58-Diplom-Basic
photos = vk.all_photos() - предоставляет dict самых больших по размеру фотографий в виде:
{'17':{'likes':17, 'type' z, 'url'}}
Фотографии, с одинаковым количеством лайков записываются с нумерацией '17(2)', '17(3)'.


albums = vk.get_albums() - предоставляет dict альбомов пользователя в виде: 
'str' :{'album_id: int, 'photos_quantity': int}}.

photos_from_any_album = vk.all_photos_from_album(album_id: int) - предоставляет dict в виде
{'17':{'likes':17, 'type' z, 'url'}}
Фотографии, с одинаковым количеством лайков записываются с нумерацией '17(2)', '17(3)'
все в рамках определнного альбома.

print(ya.bu_all_photos_to_disk(photos_from_any_album, quantity=int, album_name=str))
принимает dict в формате {'17':{'likes':17, 'type' z, 'url'}}
photos_quantity - по умолчанию 5, можно ставить любое, но не превышающее len(dict).
album_name - папка на яндекс диске в которую будут скачиваться фотографии. указывается без '/'
по умолчанию используется текущая дата.


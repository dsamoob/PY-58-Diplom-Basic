import requests
from tqdm import tqdm
from datetime import datetime
import json


class YandexDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files?limit=1000'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        response_href = self._get_upload_link(disk_file_path=disk_file_path)
        print(response_href)
        url = response_href.get("href", "")
        response = requests.put(url, data=open(filename, 'rb'))
        print(response)
        response.raise_for_status()
        if response.status_code == 201:
            print('success')

    def bu_all_photos_to_disk(self, dict_with_names_url=None, quantity=5, album_name=str(datetime.now()).split()[0]):
        if len(dict_with_names_url) < quantity:
            return f'incorrect photos quantity'
        updated_photos_list = {}
        result_of_uploading = []
        for number, (key, value) in enumerate(dict_with_names_url.items()):
            if number == quantity:
                break
            updated_photos_list[key] = value
        self._make_new_directory(album_name)
        count = 0
        for name, info in tqdm(updated_photos_list.items()):
            if count < quantity:
                response_href = self._get_upload_link(f'{album_name}/{name}.jpg')
                url = response_href.get("href", "")
                download_link = requests.get(info['url'])
                response = requests.put(url, data=download_link.content)
                response.raise_for_status()
                count += 1
                if response.status_code == 201:
                    result_of_uploading.append({'file_name': name, 'file_type': info['type'], 'upload_status': 'success'})
                else:
                    result_of_uploading.append(
                        {'file_name': name, 'file_type': info['type'], 'upload_status': 'not uploaded'})
        with open("result.json", "w", encoding="utf-8") as file:
            json.dump(result_of_uploading, file)
        return result_of_uploading

    def _make_new_directory(self, dirname: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {"path": dirname, "overwrite": "true"}
        response = requests.put(url, headers=headers, params=params)
        response.raise_for_status()
        if response.status_code == 201:
            print(f'directory with name: {dirname} is ready')

    def delete_file(self, file):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        response = requests.delete(f'{url}?path={file}', headers=headers)
        response.raise_for_status()
        if response.status_code == 204:
            print('success')

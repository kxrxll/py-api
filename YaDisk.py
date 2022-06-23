import requests


class Ya_disk:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        print(response.json())
        return response.json()

    def upload(self, path, url):
        headers = self.get_headers()
        params = {
            "path": path,
            "url": url
        }
        response = requests.post("https://cloud-api.yandex.net/v1/disk/resources/upload", params=params, headers=headers)
        response.raise_for_status()

import requests


class Vk_api:
    def __init__(self, token: str):
        self.token = token

    def _get_params(self):
        return {
            "access_token": self.token,
            "photo_sizes": 1,
            "v": 5.81
        }

    def get_images(self):
        params = self._get_params()
        response = requests.get("https://api.vk.com/method/photos.getAll", params=params)
        response.raise_for_status()
        print(response.json())
        result_response = response.json()["response"]["items"]
        result = []
        for item in result_response:
            result.append({
                "id": item["id"],
                "url": max(item["sizes"], key=lambda x: x["width"])["url"]
            })
        return result

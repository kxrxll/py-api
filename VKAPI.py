import requests
from datetime import datetime


class Vk_api:
    def __init__(self, token: str, owner):
        self.token = token
        if type(owner) == int:
            self.owner_id = owner
        else:
            self.owner_name = owner
            self.owner_id = self._get_id()

    def _get_params_for_id(self):
        return {
            "access_token": self.token,
            "v": 5.81,
            "owner_id": self.owner_id,
            "extended": 1
        }

    def _get_params_for_name(self):
        return {
            "access_token": self.token,
            "v": 5.81,
            "user_ids": self.owner_name
        }

    def _get_id(self):
        params = self._get_params_for_name()
        response = requests.get("https://api.vk.com/method/users.get", params=params)
        response.raise_for_status()
        return response.json()["response"][0]["id"]

    def get_images(self):
        params = self._get_params_for_id()
        response = requests.get("https://api.vk.com/method/photos.getAll", params=params)
        response.raise_for_status()
        result_response = response.json()["response"]["items"]
        result = []
        for item in result_response:
            result.append({
                "id": item["id"],
                "date": datetime.fromtimestamp(item["date"]).strftime("%d_%m_%y"),
                "likes": item["likes"]["count"],
                "url": max(item["sizes"], key=lambda x: x["width"])["url"]
            })
        return result
